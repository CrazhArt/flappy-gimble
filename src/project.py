"""
Simple python survival game
Run: python project.py
"""

import pygame
import random


# --- Constants -----------------------------------------------------------------

screen_width = 1920
screen_height = 1080

character_width = 100
character_height = 100

# --- Main ----------------------------------------------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("Flappy Gimble")

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    dt = 0

    score = 0

    running = True
    while running:
        bg = pygame.image.load("Assets/defaultBG.png")
        screen.blit(bg, (0,0))

        pygame.display.flip

        dt = clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()