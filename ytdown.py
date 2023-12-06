import csv
import threading
from pytube import YouTube
AUDIO_DOWNLOAD_DIR = "../yt-to-mp4/songs"

def YoutubeAudioDownload(video_url):
  video = YouTube(video_url)
  audio = video.streams.filter(only_audio = True).first()

  try:
      audio.download(AUDIO_DOWNLOAD_DIR)
  except:
      print("Failed to download audio")

  print(f"\naudio {video_url} was downloaded successfully")

if __name__ == '__main__':
    with open('../yt-to-mp4/links.csv', mode='r') as file:
        r = csv.reader(file)
        for row in r:
            t = threading.Thread(target=YoutubeAudioDownload, args=(str(row[0]), ))
            t.start()
