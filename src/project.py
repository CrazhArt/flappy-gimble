"""
Simple python survival game
Run: python flappy_gimble.py
"""

import pygame
import random


# --- Constants -----------------------------------------------------------------

canvasw = 1920
canvash = 1080

# --- Main ----------------------------------------------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("Flappy Gimble")

    screen = pygame.display.set_mode((canvasw, canvash))
    clock = pygame.time.Clock()

if __name__ == "__main__":
    main()