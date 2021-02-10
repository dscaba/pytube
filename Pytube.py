import os
import time
import sys
import re

try:
    from pytube import YouTube
    from pytube import request
    from pytube.cli import on_progress
    from art import *
except ImportError:
    import subprocess
    subprocess.run("pip install pytube art")
    from pytube import YouTube
    from pytube import request
    from pytube.cli import on_progress
    from art import *
    
fig = text2art("YouTube Downloader")
print(fig)

url = input("Ingrese el link del video a descargar: ")


yt = YouTube(url, on_progress_callback=on_progress)


user = os.getlogin()

location = "C:\\Users\\" + user + "\\Desktop"




print("¿Qué desea descargar?"'\n')
print("1 - Video Completo") 
print("2 - Solo audio"'\n') 
choice = int(input("Elija la opción deseada: "))
while True:
    if choice == 1:
        print("Usted Descargará el siguiente video: ", yt.title)
        yt.streams.get_highest_resolution().download(location)
        print("La descaga ha comenzado..."'\n')

        print("Descarga completada ✔")
        break
    elif choice == 2:
        print("Usted Descargará el audio siguiente video: ", yt.title)
        yt.streams.get_audio_only(subtype="mp4").download(location)
        print("La descaga ha comenzado..."'\n')
    
        print("Descarga realizada con éxito!")
        break

time.sleep(3)
