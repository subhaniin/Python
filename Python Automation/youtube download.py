import yt_dlp

def list_formats(url):
    with yt_dlp.YoutubeDL({}) as ydl:
        try:
            ydl.download([f'-F', url])
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")

video_url = 'https://www.youtube.com/watch?v=5OdVJbNCSso'
list_formats(video_url)
