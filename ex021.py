"""
Desafio 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
print('='*10, ' DESAFIO 021 - Resolução - Aula 08 - Pygame ', '='*10)
# Este foi o metodo explicado na aula, para o pygame funcionar, será preciso iniciar o mesmo com pygame.init()

import pygame
pygame.init()
pygame.mixer.music.load('warcraft.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('='*30)

print('='*10, ' Existe o Playsound ', '='*10)
import playsound
playsound.playsound('warcraft.mp3')

print('='*30)

print('='*10, ' Também existe o WebBrowser ', '='*10)
import webbrowser
webbrowser.open("warcraft.mp3")
