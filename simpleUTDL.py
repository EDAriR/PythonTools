from __future__ import unicode_literals
import youtube_dl

ydl_opts = {'outtmpl': 'download/%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=HTZ5xn12AL4'])