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

# --- Custom Functions ----------------------------------------------------------

# Draws text on the screen
def drawText(text, typeface, color, x_coord, y_coord):
    image = typeface.render(text, True, color)
    SCREEN.blit(image, (x_coord, y_coord))

# Restarts the game after a gameover; resets player location and score
def resetGame():
    leafGroup.empty()
    player.rect.x = 200
    player.rect.y = int(SCREEN_HEIGHT / 2)
    playerScore = 0
    return playerScore


# --- Classes -------------------------------------------------------------------


# Main player class
class Gimble(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        pygame.sprite.Sprite.__init__(self)

        # Where sprite frames are held and iterated
        self.sprite_frames = []
        self.index = 0
        self.counter = 0

        # Scrolls through & animates frames
        for i in range(1,5):
            image = pygame.image.load(f"Assets/Player/defaultCHAR{i}.png")
            self.sprite_frames.append(image)
        self.image = self.sprite_frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x_coord, y_coord]

        # Velocity default constants
        self.velocity = 0
        self.pressed = False

    def update(self):
        # Increases gravity velocity while running
        if flying == True:
            self.velocity += 2
            if self.velocity > 20:
                self.velocity = 20
            # Minimum height to maintain before death
            if self.rect.bottom < (SCREEN_HEIGHT - 200):
                self.rect.y += int(self.velocity)

        # Click to jump mechanic
        if gameOver == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                self.velocity = -20
            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False

            # Animation loop
            self.counter += 1
            animCooldown = 1
            # Resets counter once reaching final image
            if self.counter > animCooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.sprite_frames):
                    self.index = 0
            self.image = self.sprite_frames[self.index]

            # Rotates character sprite while flying
            self.image = pygame.transform.rotate(self.sprite_frames[self.index], self.velocity * -2)
        # Rotates character sprite when dead
        else:
            self.image = pygame.transform.rotate(self.sprite_frames[self.index], -90)


# Main obstacle class
class Leaves(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, pos):
        pygame.sprite.Sprite.__init__(self)

        # Draws image on screen
        self.image = pygame.image.load('Assets/Stalagmite.png')
        self.rect = self.image.get_rect()

        # Defines upper and lower pipes w/ gap
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x_coord, y_coord - int(GAP/2)]
        if pos == -1:
            self.rect.topleft = [x_coord, y_coord + int(GAP/2)]

    def update(self):
        # Scrolls image to the left
        self.rect.x -= scrollSpeed

        # Kills object once completely off screen
        if self.rect.right < 0:
            self.kill()


# Restart button
class Button():
    # Draws image on screen
    def __init__(self, x_coord, y_coord, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_coord, y_coord)

    def draw(self):
        reset = False

        # Gets position of cursor
        pos = pygame.mouse.get_pos()

        # Checks if cursor collides w/ drawn image and is clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                reset = True

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return reset


# --- Main ----------------------------------------------------------------------


# Initialization & Images
pygame.init()
pygame.display.set_caption("Flappy Gimble")
clock = pygame.time.Clock()
black = (0, 0 ,0)
typeface = pygame.font.SysFont("xolonium", 75)
bg = pygame.image.load("Assets/Background.png")
fg = pygame.image.load("Assets/Foreground.png")
button = pygame.image.load("Assets/Restart.png")

# Default settings
baseScroll = 0
scrollSpeed = 20
flying = False
gameOver = False
score = 0
passPile = False

# Groups and group settings
playerGroup = pygame.sprite.Group()
leafGroup = pygame.sprite.Group()
lastLeaf = pygame.time.get_ticks() - SPAWN_INTERVAL
player = Gimble(int(SCREEN_WIDTH/4), int(SCREEN_HEIGHT/2))
playerGroup.add(player)
restartButton = Button((SCREEN_WIDTH/2) - 250, 125, button)

running = True

# Main function
while running:
    clock.tick(FPS)

    # Draws images on screen
    SCREEN.blit(bg, (0,0))

    playerGroup.draw(SCREEN)
    playerGroup.update()

    leafGroup.draw(SCREEN)

    # Scrolls ground
    SCREEN.blit(fg, (baseScroll, (SCREEN_HEIGHT - 200)))

    # Checks if player sprite passes through obstacles
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

    # Checks if player and obstacles collide
    if pygame.sprite.groupcollide(playerGroup, leafGroup, False, False) or player.rect.top < 0:
        gameOver = True

    # Checks if player collides w/ ground
    if player.rect.bottom > (SCREEN_HEIGHT - 200):
        gameOver = True
        flying = False

    # Generates new obstacles while running
    if gameOver == False and flying == True:
        timeNow = pygame.time.get_ticks()
        if timeNow - lastLeaf > SPAWN_INTERVAL:
            leafHeight = random.randint(-350, 150)
            bottomLeaf = Leaves(SCREEN_WIDTH, int(SCREEN_HEIGHT/2) + leafHeight, -1)
            topLeaf = Leaves(SCREEN_WIDTH, int(SCREEN_HEIGHT/2) + leafHeight, 1)
            leafGroup.add(bottomLeaf)
            leafGroup.add(topLeaf)
            lastLeaf = timeNow

        # Scrolls ground while running
        baseScroll -= scrollSpeed
        if abs(baseScroll) > 1920:
            baseScroll = 0

        leafGroup.update()

    # Draws restart button when gameover; resets game if clicked
    if gameOver == True:
        if restartButton.draw() == True:
            gameOver = False
            score = resetGame()

    # Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameOver == False:
            flying = True

    pygame.display.update()

pygame.quit()