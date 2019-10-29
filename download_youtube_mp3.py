""" Download video from youtube given url """
from __future__ import unicode_literals
import sys
import youtube_dl

OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


with youtube_dl.YoutubeDL(OPTIONS) as youtube:
    youtube.download([sys.argv[1]])
