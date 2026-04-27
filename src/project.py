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
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GAP = 350
SPAWN_INTERVAL = 2250 # Interval in milliseconds

black = (0, 0 ,0)

# --- Custom Functions ----------------------------------------------------------


def drawText(text, typeface, color, x_coord, y_coord):
    image = typeface.render(text, True, color)
    SCREEN.blit(image, (x_coord, y_coord))

def resetGame():
    leafGroup.empty()
    player.rect.x = 200
    player.rect.y = int(SCREEN_HEIGHT / 2)
    playerScore = 0
    return playerScore


# --- Classes -------------------------------------------------------------------


class Gimble(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_frames = []
        self.index = 0
        self.counter = 0

        for i in range(1,5):
            image = pygame.image.load(f"Assets/Player/defaultCHAR{i}.png")
            self.sprite_frames.append(image)
        self.image = self.sprite_frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x_coord, y_coord]

        self.velocity = 0
        self.pressed = False

    def update(self):
        if flying == True:
            self.velocity += 2
            if self.velocity > 20:
                self.velocity = 20
            if self.rect.bottom < (SCREEN_HEIGHT - 250):
                self.rect.y += int(self.velocity)

        if gameOver == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                self.velocity = -20
            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False

            self.counter += 1
            animCooldown = 1
            if self.counter > animCooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.sprite_frames):
                    self.index = 0
            self.image = self.sprite_frames[self.index]

            self.image = pygame.transform.rotate(self.sprite_frames[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.sprite_frames[self.index], -90)


class Leaves(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Assets/defaultPIPE.png')
        self.rect = self.image.get_rect()

        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x_coord, y_coord - int(GAP/2)]
        if pos == -1:
            self.rect.topleft = [x_coord, y_coord + int(GAP/2)]

    def update(self):
        self.rect.x -= scrollSpeed

        if self.rect.right < 0:
            self.kill()


class Button():
    def __init__(self, x_coord, y_coord, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_coord, y_coord)

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return action


# --- Main ----------------------------------------------------------------------


pygame.init()
pygame.display.set_caption("Flappy Gimble")
clock = pygame.time.Clock()
typeface = pygame.font.SysFont("xolonium", 75)
bg = pygame.image.load("Assets/defaultBG.png")
fg = pygame.image.load("Assets/defaultFG.png")
button = pygame.image.load("Assets/defaultRESTART.png")

baseScroll = 0
scrollSpeed = 20
flying = False
gameOver = False
lastLeaf = pygame.time.get_ticks() - SPAWN_INTERVAL
score = 0
passPile = False

playerGroup = pygame.sprite.Group()
leafGroup = pygame.sprite.Group()
player = Gimble(int(SCREEN_WIDTH/4), int(SCREEN_HEIGHT/2))
playerGroup.add(player)
restartButton = Button((SCREEN_WIDTH/2) - 150, 150, button)

running = True

while running:
    clock.tick(FPS)

    SCREEN.blit(bg, (0,0))

    playerGroup.draw(SCREEN)
    playerGroup.update()

    leafGroup.draw(SCREEN)

    SCREEN.blit(fg, (baseScroll, (SCREEN_HEIGHT - 250)))

    if len(leafGroup) > 0:
        if playerGroup.sprites()[0].rect.left > leafGroup.sprites()[0].rect.left\
            and playerGroup.sprites()[0].rect.left < leafGroup.sprites()[0].rect.right\
                and passPile == False:
                passPile = True
        if passPile == True:
            if playerGroup.sprites()[0].rect.left > leafGroup.sprites()[0].rect.right:
                score += 1
                passPile = False

    drawText(str(score), typeface, black, int(SCREEN_WIDTH/2) - 25, 25)

    if pygame.sprite.groupcollide(playerGroup, leafGroup, False, False) or player.rect.top < 0:
        gameOver = True

    if player.rect.bottom > (SCREEN_HEIGHT - 250):
        gameOver = True
        flying = False

    if gameOver == False and flying == True:
        timeNow = pygame.time.get_ticks()
        if timeNow - lastLeaf > SPAWN_INTERVAL:
            leafHeight = random.randint(-300, 100)
            bottomLeaf = Leaves(SCREEN_WIDTH, int(SCREEN_HEIGHT/2) + leafHeight, -1)
            topLeaf = Leaves(SCREEN_WIDTH, int(SCREEN_HEIGHT/2) + leafHeight, 1)
            leafGroup.add(bottomLeaf)
            leafGroup.add(topLeaf)
            lastLeaf = timeNow

        baseScroll -= scrollSpeed
        if abs(baseScroll) > 70:
            baseScroll = 0

        leafGroup.update()

    if gameOver == True:
        if restartButton.draw() == True:
            gameOver = False
            score = resetGame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameOver == False:
            flying = True

    pygame.display.update()

pygame.quit()