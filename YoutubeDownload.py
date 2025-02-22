import os
import yt_dlp

# Set FFmpeg path manually (if not added to system PATH)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

video_url = "Your video URL here"

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': 'downloaded_video.mp4',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download complete!")