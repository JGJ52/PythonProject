import pygame, tkinter
from tkinter import ttk

path = "/home/jgj52/Music/Eurovision Ringtone.mp3"

pygame.init()
pygame.mixer.init()

def play(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

tk = tkinter.Tk()
tk.title("Music Player")

playButton = tkinter.Button(tk,text="Play",command=lambda: play(path))
stopButton = tkinter.Button(tk,text="Stop",command=stop)
volumeSlider = tkinter.Scale(tk,from_=0,to=100,orient="horizontal",label="Volume",command=volume)
playButton.pack()
stopButton.pack()
volumeSlider.pack()

style = ttk.Style()
style.theme_use("clam")

tk.mainloop()