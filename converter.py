import os
import yt_dlp

def download_youtube_video(url, save_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading: {url}")
        try:
            ydl.download([url])
        except Exception as e:
            print(f"An error occurred during the download: {e}")

def main():
    url = input("Enter the YouTube video URL: ")
    print(f"URL entered: {url}")

    save_path = "/home/c-sar-oliveira/Music"

    if not os.path.exists(save_path):
        print(f"The folder {save_path} does not exist. Creating the folder.")
        os.makedirs(save_path)

    download_youtube_video(url, save_path)
    print("Download and conversion completed! Check the specified folder.")

if __name__ == "__main__":
    main()
