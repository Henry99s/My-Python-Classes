import pygame

print('=====Reproduzindo um arquivo MP3=====')

# Abrindo o Modulo pygame
pygame.init()
pygame.mixer.music.load('Exercicio21-musica.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


