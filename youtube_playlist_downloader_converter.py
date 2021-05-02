# https://pytube.io/en/latest/user/playlist.html
# https://jun-itworld.tistory.com/37
# https://github.com/modkhi/yt-playlist/blob/master/yt-playlist-download.py
from pytube import Playlist
import pytube
import os
import subprocess

# 주의: 실행경로에 주의할 것. ffmpeg.exe가 있는 경로에서 실행해야 함.
p = Playlist('플레이리스트URL')
download_dir='원하는위치\download'
convert_dir='원하는위치\playlist'

print(f'Downloading PlayList: {p.title}')
for video in p.videos:
    ## 유튜브 플레이리스트 동영상 다운로드
    music=video.streams.first()
    default_filename=music.default_filename
    print("Downloading Video " + default_filename + "...")
    music.download(download_dir)
    
    ## 동영상 -> mp3 변환
    new_filename = default_filename[0:-3] + "mp3"
    print("Converting to mp3...")
    subprocess.run(['ffmpeg', '-i', 
        os.path.join(download_dir, default_filename),
        os.path.join(convert_dir, new_filename) ])

print("Download finished.")