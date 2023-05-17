import pygame
from random import randint

pygame.init()

music = ["soundTestFiles/bravo.mp3", "soundTestFiles/COMET_demo.mp3", "soundTestFiles/SPACE_JAMZdemo3.mp3"]


pygame.mixer.music.load(music[int(input("wha3t track do you want to listen to? (1-3)")) - 1])

pygame.mixer.music.play()

pygame.time.wait(10000)

pygame.quit()

