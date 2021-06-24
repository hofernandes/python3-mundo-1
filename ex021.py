# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# from pygame import (mixer,event)
# mixer.init()
# mixer.music.load('ex021.mp3')
# mixer.music.play()
# input('CURTE O SOM PIVETE!')

# import os, time
# os.startfile(r'ex021.mp3')
# time.sleep(10)

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()

# from playsound import playsound
# playsound('ex021.mp3')