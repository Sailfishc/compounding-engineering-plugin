---
name: youtube-downloader
description: "Download videos from YouTube and 1000+ other platforms with quality selection, format conversion, and metadata preservation. Use when users request to download, fetch, or save videos from URLs. Supports single videos, playlists, batch downloads, quality selection (480p-4K), multiple formats (MP4/WebM), audio extraction (MP3), and automatic metadata/thumbnail saving. Default output is ~/Downloads directory."
---

# YouTube Downloader

## Overview

Download videos from YouTube and 1000+ supported platforms including Vimeo, Twitter, Instagram, TikTok, Bilibili, and more. Provides fine-grained control over quality, format, and metadata preservation.

## Quick Start

### Single Video Download

```bash
# Best quality to ~/Downloads
python scripts/download_video.py "https://youtube.com/watch?v=VIDEO_ID"

# Specific quality and format
python scripts/download_video.py "URL" --quality 1080 --format mp4

# Custom output directory
python scripts/download_video.py "URL" --output /path/to/folder
```

### Batch Download

```bash
# Create a text file with URLs (one per line)
echo "https://youtube.com/watch?v=VIDEO1" > urls.txt
echo "https://youtube.com/watch?v=VIDEO2" >> urls.txt

# Download all
python scripts/batch_download.py urls.txt --quality 720
```

## Core Capabilities

### 1. Quality Selection

Choose video resolution based on needs:

```bash
# Standard Definition
--quality 480

# HD
--quality 720

# Full HD
--quality 1080

# 2K
--quality 1440

# 4K Ultra HD
--quality 4k

# Highest available (default)
--quality best
```

**Note:** Final quality depends on source availability. If 4K is requested but only 1080p is available, downloads the highest available quality.

### 2. Format Options

```bash
# MP4 (most compatible, recommended)
--format mp4

# WebM (good compression)
--format webm

# MKV (supports subtitles)
--format mkv

# Audio only (MP3)
--audio-only
```

### 3. Playlist Downloads

Playlists are automatically detected and downloaded sequentially:

```bash
python scripts/download_video.py "https://youtube.com/playlist?list=PLAYLIST_ID"
```

Each video in the playlist downloads with its own metadata and thumbnail.

### 4. Metadata Preservation

By default, saves comprehensive metadata for each video:

**Files created:**
- `video.mp4` - The video file
- `video.info.json` - Complete metadata (title, description, uploader, duration, views, etc.)
- `video.jpg` - Thumbnail image (embedded in video)

**Disable metadata:**
```bash
--no-metadata      # Skip JSON file
--no-thumbnail     # Skip thumbnail
```

### 5. Batch Processing

Create a text file with URLs (one per line):

```
https://youtube.com/watch?v=VIDEO1
https://youtube.com/watch?v=VIDEO2
# Comments start with #
https://youtube.com/playlist?list=PLAYLIST_ID
```

Then download all:

```bash
python scripts/batch_download.py urls.txt --quality 720 --format mp4
```

## Common Use Cases

### Download lecture series in 720p
```bash
python scripts/download_video.py "PLAYLIST_URL" --quality 720 --format mp4
```

### Extract audio from music videos
```bash
python scripts/download_video.py "URL" --audio-only
```

### Archive videos with full metadata
```bash
python scripts/download_video.py "URL" --quality best
# Creates: video.mp4, video.info.json, video.jpg
```

### Download to custom location
```bash
python scripts/download_video.py "URL" --output ~/Videos/Courses
```

### Batch download reading list
```bash
# Create urls.txt with video links
python scripts/batch_download.py urls.txt --quality 1080 --output ~/Videos
```

## Supported Platforms

The skill supports 1000+ websites via yt-dlp. Most common platforms:

- **YouTube** - Videos, playlists, channels, live streams
- **Vimeo** - Videos, user channels
- **Twitter/X** - Video tweets
- **Instagram** - Videos, stories, reels
- **TikTok** - Videos
- **Bilibili** - Videos (Chinese platform)
- **Facebook** - Public videos
- **Twitch** - VODs, clips, streams
- **Reddit** - Video posts

For complete platform list, see `references/platforms_and_formats.md`

## Script Reference

### download_video.py

Main download script with full feature support.

**Arguments:**
- `url` - Video or playlist URL (required)
- `-o, --output` - Output directory (default: ~/Downloads)
- `-q, --quality` - Video quality: 480, 720, 1080, 1440, 4k, best (default: best)
- `-f, --format` - Output format: mp4, webm, mkv (default: mp4)
- `-a, --audio-only` - Download audio only as MP3
- `--no-metadata` - Skip metadata JSON file
- `--no-thumbnail` - Skip thumbnail download

### batch_download.py

Download multiple videos from a URL list.

**Arguments:**
- `urls_file` - Text file with URLs (one per line, # for comments)
- `-o, --output` - Output directory (default: ~/Downloads)
- `-q, --quality` - Video quality for all downloads
- `-f, --format` - Output format for all downloads
- `-a, --audio-only` - Download all as audio

## Dependencies

The script auto-installs required dependencies:
- `yt-dlp` - Video download engine
- `ffmpeg` - Required for format conversion and audio extraction (system package)

If ffmpeg is not installed, run:
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

## Troubleshooting

**Download fails with "Unable to extract":**
- Platform may require authentication
- Video may be private or region-locked
- Try updating yt-dlp: `pip install -U yt-dlp --break-system-packages`

**Audio extraction fails:**
- Install ffmpeg (see Dependencies section)

**Slow download speed:**
- Some platforms throttle download speed
- Try different quality settings
- Check your internet connection

**Playlist only downloads some videos:**
- Some videos in playlist may be private or deleted
- Check batch_download output for specific errors
