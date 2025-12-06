#!/usr/bin/env python3
"""
YouTube Video Downloader using yt-dlp
Supports single videos, playlists, and quality selection
"""

import argparse
import json
import os
import sys
from pathlib import Path


def get_default_download_path():
    """Get the default Downloads directory"""
    home = Path.home()
    downloads = home / "Downloads"
    downloads.mkdir(exist_ok=True)
    return str(downloads)


def download_video(url, output_path=None, quality="best", format_type="mp4", 
                   audio_only=False, save_metadata=True, save_thumbnail=True):
    """
    Download a video from YouTube or other supported platforms
    
    Args:
        url: Video or playlist URL
        output_path: Directory to save downloads (default: ~/Downloads)
        quality: Video quality (480, 720, 1080, 1440, 2160/4k, or 'best')
        format_type: Output format (mp4, webm, mkv)
        audio_only: Download only audio (mp3)
        save_metadata: Save video metadata as JSON
        save_thumbnail: Save video thumbnail
    """
    try:
        import yt_dlp
    except ImportError:
        print("Installing yt-dlp...")
        os.system(f"{sys.executable} -m pip install -U yt-dlp --break-system-packages -q")
        import yt_dlp
    
    # Set output path
    if output_path is None:
        output_path = get_default_download_path()
    
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Configure quality
    quality_map = {
        '480': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        '720': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        '1080': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '1440': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
        '2160': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
        '4k': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
        'best': 'bestvideo+bestaudio/best'
    }
    
    # Build yt-dlp options
    ydl_opts = {
        'outtmpl': str(output_path / '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
    }
    
    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts['format'] = quality_map.get(str(quality), quality_map['best'])
        if format_type:
            ydl_opts['merge_output_format'] = format_type
    
    # Metadata and thumbnail options
    if save_metadata:
        ydl_opts['writeinfojson'] = True
    
    if save_thumbnail:
        ydl_opts['writethumbnail'] = True
        ydl_opts['postprocessors'] = ydl_opts.get('postprocessors', [])
        ydl_opts['postprocessors'].append({
            'key': 'EmbedThumbnail',
        })
    
    # Download
    print(f"Downloading to: {output_path}")
    print(f"URL: {url}")
    print(f"Quality: {quality}")
    print(f"Format: {'audio-only (mp3)' if audio_only else format_type}")
    print("-" * 60)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            
            # Print summary
            if info:
                if 'entries' in info:  # Playlist
                    print(f"\n✅ Downloaded {len(info['entries'])} videos from playlist")
                else:  # Single video
                    print(f"\n✅ Downloaded: {info.get('title', 'Video')}")
                    print(f"   Duration: {info.get('duration', 0) // 60}m {info.get('duration', 0) % 60}s")
                    if 'filesize' in info and info['filesize']:
                        print(f"   Size: {info['filesize'] / 1024 / 1024:.1f} MB")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Download failed: {str(e)}", file=sys.stderr)
            return False


def main():
    parser = argparse.ArgumentParser(
        description='Download videos from YouTube and other platforms',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download single video in best quality
  %(prog)s "https://youtube.com/watch?v=VIDEO_ID"
  
  # Download in 720p as MP4
  %(prog)s "URL" --quality 720 --format mp4
  
  # Download audio only
  %(prog)s "URL" --audio-only
  
  # Download to specific directory
  %(prog)s "URL" --output /path/to/folder
  
  # Download entire playlist
  %(prog)s "https://youtube.com/playlist?list=PLAYLIST_ID"
  
  # Download in 4K without metadata
  %(prog)s "URL" --quality 4k --no-metadata --no-thumbnail
        """
    )
    
    parser.add_argument('url', help='Video or playlist URL')
    parser.add_argument('-o', '--output', help='Output directory (default: ~/Downloads)')
    parser.add_argument('-q', '--quality', 
                        choices=['480', '720', '1080', '1440', '2160', '4k', 'best'],
                        default='best',
                        help='Video quality (default: best)')
    parser.add_argument('-f', '--format', 
                        choices=['mp4', 'webm', 'mkv'],
                        default='mp4',
                        help='Output format (default: mp4)')
    parser.add_argument('-a', '--audio-only', 
                        action='store_true',
                        help='Download audio only (MP3)')
    parser.add_argument('--no-metadata', 
                        action='store_true',
                        help='Do not save metadata JSON')
    parser.add_argument('--no-thumbnail', 
                        action='store_true',
                        help='Do not save thumbnail')
    
    args = parser.parse_args()
    
    success = download_video(
        url=args.url,
        output_path=args.output,
        quality=args.quality,
        format_type=args.format,
        audio_only=args.audio_only,
        save_metadata=not args.no_metadata,
        save_thumbnail=not args.no_thumbnail
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
