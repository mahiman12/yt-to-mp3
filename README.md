# YT-to-MP4
[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Standalone script written in Python 3 to convert youtube videos to MP4 from a given list of youtube URLs.

## Install

The script has 1 dependency:

*   [pytube](https://pypi.org/project/pytube/)

You can install it by typing:

```
pip install -r requirements.txt
```

## Configuration

The **links.csv** file contains the Youtube URLs and has to be ordered in the file in this way
<p align="left"><img width="137" alt="Screenshot 2023-12-06 at 11 25 00" src="https://github.com/mahiman12/yt-to-mp4/assets/44576514/1f3cf4d5-4eaf-4509-a037-507f1bd2c2c8"></p>

**NOTE:** In case you need to make this list from a playlist, there is a [website](https://www.thetubelab.com/get-all-urls-of-youtube-playlist-channel/ "website") that provides the URLs of all the videos in the playlist. You can paste the link of your youtube playlist there, and straighaway copy-paste the URLs of all the videos in the **links.csv** file.

## Run

```
python ytdown.py 

```
