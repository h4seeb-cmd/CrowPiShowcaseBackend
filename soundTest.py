import pygame


pygame.init()

pygame.mixer.music.load("soundTestFiles/bravo.mp3")

pygame.mixer.music.play()

pygame.time.wait(10000)

pygame.quit()


