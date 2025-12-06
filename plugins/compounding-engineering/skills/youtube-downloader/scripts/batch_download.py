#!/usr/bin/env python3
"""
Batch download videos from a list of URLs
"""

import argparse
import sys
from pathlib import Path
from download_video import download_video


def batch_download(urls_file, output_path=None, quality="best", 
                   format_type="mp4", audio_only=False):
    """
    Download multiple videos from a file containing URLs
    
    Args:
        urls_file: Path to text file with one URL per line
        output_path: Directory to save downloads (default: ~/Downloads)
        quality: Video quality
        format_type: Output format
        audio_only: Download only audio
    """
    urls_file = Path(urls_file)
    
    if not urls_file.exists():
        print(f"❌ File not found: {urls_file}", file=sys.stderr)
        return False
    
    # Read URLs
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not urls:
        print("❌ No URLs found in file", file=sys.stderr)
        return False
    
    print(f"Found {len(urls)} URLs to download")
    print("=" * 60)
    
    # Download each URL
    success_count = 0
    failed_urls = []
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")
        print("-" * 60)
        
        if download_video(url, output_path, quality, format_type, audio_only):
            success_count += 1
        else:
            failed_urls.append(url)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"✅ Successfully downloaded: {success_count}/{len(urls)}")
    
    if failed_urls:
        print(f"❌ Failed: {len(failed_urls)}")
        print("\nFailed URLs:")
        for url in failed_urls:
            print(f"  - {url}")
    
    return len(failed_urls) == 0


def main():
    parser = argparse.ArgumentParser(
        description='Batch download videos from a URL list',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
URL File Format:
  One URL per line
  Lines starting with # are treated as comments
  
Example:
  https://youtube.com/watch?v=VIDEO1
  https://youtube.com/watch?v=VIDEO2
  # This is a comment
  https://youtube.com/playlist?list=PLAYLIST_ID
        """
    )
    
    parser.add_argument('urls_file', help='Text file containing URLs (one per line)')
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
    
    args = parser.parse_args()
    
    success = batch_download(
        urls_file=args.urls_file,
        output_path=args.output,
        quality=args.quality,
        format_type=args.format,
        audio_only=args.audio_only
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
