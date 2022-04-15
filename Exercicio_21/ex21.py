import pygame
pygame.init()

pygame.mixer.music.load("..\\resource\\music.mp3")
pygame.mixer.music.play()
pygame.event.wait()
