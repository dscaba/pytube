import os
import time
from pytube import YouTube
from art import *

fig = text2art("YouTube Downloader")
print(fig)

link = input("Ingrese el link del video a descargar: ")
yt = YouTube(link)
user = os.getlogin()

location = "C:\\Users\\" + user + "\\Desktop"


print("¿Qué desea descargar?"'\n')
print("1 - Video Completo") 
print("2 - Solo audio"'\n') 
choice = int(input("Elija la opción deseada: "))
while True:
    if choice == 1:
        print("Usted Descargará el siguiente video: ", yt.title)
        ys = yt.streams.get_highest_resolution()
        print("La descaga ha comenzado..."'\n')
        ys.download(location)
        print("Descarga completada ✔")
        break
    elif choice == 2:
        print("Usted Descargará el audio siguiente video: ", yt.title)
        ys = yt.streams.get_audio_only(subtype="mp4")
        print("La descaga ha comenzado..."'\n')
        ys.download(location)
        print("Descarga realizada con éxito!")
        break

time.sleep(3)