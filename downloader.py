import os
import time
from pytube import YouTube

def Download(link):

    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()

    try:
        video_title = yt.title
        video_title = video_title.replace('/', '_')
        video_title=video_title.replace('|', '_')
        folder_name='downloaded_videos'
        filename=f"{video_title}.mp4"

        file_path = os.path.join(folder_name, filename)
        if os.path.exists(file_path):
            print(f"{filename} already exists")
            overwrite = input("Do you want to overwrite it? (Yes or No) \n")
            if overwrite.lower() == "yes" or "y":
                print("Download aborted")
                return
            
        yt.download(output_path=folder_name, filename=filename)
        print("Download is completed")
    except Exception as e:
        print("An error occurred while downloading the video", e)
        time.sleep(1)
        # os.system('cls')

def main():
    print("-" * 20 + " Youtube To MP4 Downloader " + "-" * 20)
    link = input("Enter the link of the video you want to download: ")
    Download(link)

if __name__ == "__main__":
    main()