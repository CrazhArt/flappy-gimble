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

flying = False
gameOver = False

# --- Custom Functions ----------------------------------------------------------


# --- Classes -------------------------------------------------------------------


class Gimble(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)

        self.sprite_frames = []
        self.index = 0
        self.counter = 0
        self.velocity = 0
        self.pressed = False

        for i in range(1,4):
            image = pygame.image.load(f"Assets/Player/defaultCHAR{i}.png")
            self.sprite_frames.append(image)
        self.image = self.sprite_frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)

    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.velocity > 8.5:
                self.velocity = 8.5
            if self.rect.bottom < (SCREEN_HEIGHT - 250):
                self.rect.y += int(self.velocity)

        if gameOver == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False

        self.counter += 1
        animCooldown = 3
        if self.counter > animCooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.sprite_frames):
                self.index = 0
        self.image = self.sprite_frames[self.index]

        self.image = pygame.transform.rotate(self.sprite_frames[self.index], self.velocity * 2)
        self.image = pygame.transform.rotate(self.sprite_frames[self.index], -90)

playerGroup = pygame.sprite.Group()
player = Gimble(int(SCREEN_WIDTH/4), int(SCREEN_HEIGHT/2))
playerGroup.add(player)


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