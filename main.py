# https://pytube.io/en/latest/user/playlist.html
# https://jun-itworld.tistory.com/37
# https://github.com/modkhi/yt-playlist/blob/master/yt-playlist-download.py
from pytube import Playlist
import pytube
import os
import subprocess

from tkinter import *
from tkinter import filedialog

from urllib.request import HTTPError


def Download_Convert(playlistURL,downloadDir,convertDir):
    # 주의: 실행경로에 주의할 것. ffmpeg.exe가 있는 경로에서 실행해야 함.
    p = Playlist(playlistURL)      # '플레이리스트URL'
    download_dir=downloadDir       # '원하는위치\download'
    convert_dir=convertDir         #'원하는위치\playlist'

    print(f'Downloading PlayList: {p.title}')
    for video in p.videos:
        ## 유튜브 플레이리스트 동영상 다운로드
        try:
            music=video.streams.first()
            default_filename=music.default_filename
            print("Downloading Video " + default_filename + "...")
            listBox.insert(END,default_filename)
            music.download(download_dir)
        except HTTPError as he:
            print("------- HTTPError -------")
            continue
        except KeyError as ke:
            print("------- KeyError -------")
            continue
        
        ## 동영상 -> mp3 변환
        new_filename = default_filename[0:-3] + "mp3"
        print("Converting to mp3...")
        subprocess.run(['ffmpeg', '-i', 
            os.path.join(download_dir, default_filename),
            os.path.join(convert_dir, new_filename) ])

    print("Download finished.")


def btnCmd():
    Download_Convert(ent1.get(),ent2.get(),ent3.get())    

def ask_downloadDir():
	root.dirName=filedialog.askdirectory()
	ent2.insert(0,root.dirName)

def ask_convertDir():
	root.dirName=filedialog.askdirectory()
	ent3.insert(0,root.dirName)


root=Tk()
root.title("YT Download&Convert")
root.geometry("300x200")
root.resizable(False,False)


frmTop=Frame(root)
frmTop.pack(side="top",fill="x")


## 라벨 프레임
frm1=Frame(frmTop)
frm1.pack(side="left")

lbl1=Label(frm1,text="Playlist URL")
lbl2=Label(frm1,text="Download 경로")
lbl3=Label(frm1,text="Convert 경로")
lbl1.pack()
lbl2.pack()
lbl3.pack()


## 입력창 프레임
frm2=Frame(frmTop)
frm2.pack(side="left")

ent1=Entry(frm2)
ent2=Entry(frm2)
ent3=Entry(frm2)
ent1.pack(pady=3)
ent2.pack(pady=3)
ent3.pack(pady=3)


## 입력창 프레임
frm3=Frame(frmTop)
frm3.pack(side="left")

btn=Button(frm3,text="")
btnDownDir=Button(frm3,text="...",command=ask_downloadDir)
btnConvertDir=Button(frm3,text="...",command=ask_convertDir)
btn.pack(fill="both",expand=True)
btnDownDir.pack(fill="both",expand=True)
btnConvertDir.pack(fill="both",expand=True)


## 실행 버튼
btnRun=Button(frmTop,text="실행", command=btnCmd)
btnRun.pack(fill="both",expand=True)


## 다운로드&컨버트 리스트
frmBottom=Frame(root)
frmBottom.pack(side="bottom",fill="x")

sclBar=Scrollbar(frmBottom)
sclBar.pack(side="right",fill="y")

listBox=Listbox(frmBottom,selectmode="single",yscrollcommand=sclBar.set)
listBox.pack(fill="both",expand=True)

sclBar.config(command=listBox.yview)

root.mainloop()