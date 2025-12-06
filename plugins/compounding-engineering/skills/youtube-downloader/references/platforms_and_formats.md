# Supported Platforms and Formats

## Supported Video Platforms

yt-dlp supports over 1000 websites. Here are the most common ones:

### Video Platforms
- **YouTube** - Videos, playlists, channels
- **Vimeo** - Videos, user channels
- **Dailymotion** - Videos, playlists
- **Twitter/X** - Video tweets
- **Facebook** - Public videos
- **Instagram** - Videos, stories, reels
- **TikTok** - Videos
- **Twitch** - VODs, clips
- **Reddit** - Video posts
- **Bilibili** - Videos (Chinese platform)

### Live Streaming
- **YouTube Live**
- **Twitch streams**
- **Facebook Live**

### Educational
- **Coursera** - Course videos
- **Udemy** - Course videos (if purchased)
- **Khan Academy** - Educational videos

## Quality Options

### Video Resolutions
- **480p** - SD quality (854x480)
- **720p** - HD quality (1280x720)
- **1080p** - Full HD (1920x1080)
- **1440p** - 2K quality (2560x1440)
- **2160p/4K** - Ultra HD (3840x2160)
- **best** - Highest available quality

### Format Selection
- **MP4** - Most compatible, works everywhere
- **WebM** - Open format, good compression
- **MKV** - Container format, supports subtitles

### Audio Options
- **MP3** - Audio-only download
- **M4A** - High-quality audio
- **Opus** - Efficient audio codec

## Metadata Saved

When metadata preservation is enabled, the following information is saved:

### Video Information (JSON)
- Title
- Description
- Upload date
- Uploader name and channel
- Duration
- View count
- Like count
- Tags
- Categories
- Subtitles (if available)

### Files Created
- `video.mp4` - The video file
- `video.info.json` - Metadata
- `video.jpg` - Thumbnail image
- `video.en.srt` - Subtitles (if available)

## Special Features

### Playlist Download
- Downloads all videos in order
- Preserves playlist structure
- Can set start/end indices

### Age-Restricted Content
- Handles age-restricted videos
- May require authentication for some platforms

### Subtitles
- Auto-downloads available subtitles
- Supports multiple languages
- Can embed in video file

### Post-Processing
- Automatic format conversion
- Audio extraction
- Thumbnail embedding
- Metadata tagging
