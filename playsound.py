import tkinter as tk
from tkinter import *
import pygame
import os
pygame.mixer.init()
pygame.init()
root = tk.Tk()
lista_mus = []
n = 0
p = 0
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
def check_event():
    global MUSIC_END
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            print('music end event')
            prox()
        root.after(100, check_event)
def start():
    global n
    global p
    global lista_mus
    song_name = lista_mus[n] #nome das musica // NAME OF SONGS
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(0)
    print("music started ")
    p = 0
def pause():
    global p
    p = p+1
    if p > 0:
        if p % 2 != 0:
            pygame.mixer.music.pause()
            print("Paused")

        else:
            pygame.mixer.music.unpause()

            print("unPaused")
def prox():
    global n
    n = n+1
    start()
def prev():
    global n
    n = n-1
    start()
def reload():
    global n
    start()
def check():
    global lista_mus
    path = 'C:\\Users\\User\\Documents\\mix' #caminho das musicas // PATH
    for file in os.listdir(path):
        if file.endswith(".mp3"):  #files mp3
            print(os.path.join(path, file))
            lista_mus.append( os.path.join(path, file))
class window:
    def __init__(self, root):
        self.window = root
        self.window.geometry('320x25') #tamanho da tela. // SIZE WINDOW
        self.window.resizable(width=0, height=0)
################# BOTÕES // BOTTONS #########################
        self.button = Button(self.window, text='>>', width=10, command=prox)
        self.button.grid(row=2, column=4)
        self.buttonplay = Button(self.window, text= 'play', width=10, command=start)
        self.buttonplay.grid(row=2, column= 2)

        self.buttonstop = Button(self.window, text= '||', width= 10, command=pause)
        self.buttonstop.grid(row=2, column = 3)

        self.buttonprev = Button(self.window, text='<<', width=10, command=prev)
        self.buttonprev.grid(row=2, column=1)



check()
check_event()
window(root)
root.title("sound player")
root.mainloop()
