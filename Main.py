import yt_dlp

def download_audio(url):
    # Settings
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': False,  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    video_url = input("Enter the YouTube video or playlist URL: ")
    download_audio(video_url)
