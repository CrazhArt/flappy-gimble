"""
Simple python survival game
Run: python project.py
"""

import pygame
import random
from os import walk


# --- Constants -----------------------------------------------------------------

screen_width = 1920
screen_height = 1080

# --- Custom Functions ----------------------------------------------------------


# --- Classes -------------------------------------------------------------------

class Gimble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

# class Pipe():
#     def __init__(self, pos):

# --- Main ----------------------------------------------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("Flappy Gimble")

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = pygame.image.load("Assets/defaultBG.png")
        screen.blit(bg, (0,0))

        pygame.display.flip()

        dt = clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()