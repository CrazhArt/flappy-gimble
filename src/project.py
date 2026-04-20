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

character_width = 100
character_height = 100

# --- Custom Functions ----------------------------------------------------------

def import_sprite(path):
    sprite_frames = []
    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = f"{path}/{image}"
            sprites = pygame.image.load(full_path).convert_alpha()
            sprite_frames.append(sprites)
    return sprite_frames


# --- Classes -------------------------------------------------------------------

class Gimble(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_list = []
        self.index = 0
        self.counter = 0

        self.sprites = import_sprite(f"Assets/Player")
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [screen_width//4, screen_height//2]

        self.direction = pygame.math.Vector2(0, 0)
        self.score = 0

    def animate(self):
        self.counter += 1
        animCooldown = 5
        if self.counter > animCooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.image_list):
                self.index = 0
        self.image = self.image_list[self.index]

# class Pipe():
#     def __init__(self, pos):


# --- Main ----------------------------------------------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("Flappy Gimble")

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    dt = 0

    player = pygame.sprite.GroupSingle()
    player.add(Gimble())

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = pygame.image.load("Assets/defaultBG.png")
        screen.blit(bg, (0,0))
        player.draw(screen)
        player.update()

        pygame.display.flip()

        dt = clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()