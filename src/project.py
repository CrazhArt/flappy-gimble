"""
Simple python survival game
Run: python project.py
"""

import pygame
import random


# --- Constants -----------------------------------------------------------------

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

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

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    baseScroll = 0
    scrollSpeed = 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = pygame.image.load("Assets/defaultBG.png")
        screen.blit(bg, (0,0))
        fg = pygame.image.load("Assets/defaultFG.png")
        screen.blit(fg, (baseScroll, (SCREEN_HEIGHT - 250)))
        baseScroll -= scrollSpeed
        if abs(baseScroll) > 70:
            baseScroll = 0
        pygame.display.update()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()