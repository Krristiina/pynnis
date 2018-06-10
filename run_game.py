#! /usr/bin/env python

import pygame
from sprites.player import Player
from sprites.ball import Ball
from sprites.field import Field

#screen settings
display_width = 800
display_height = 600
frames_per_second = 60

#colors
black = (0,0,0)
white = (255, 255,255)
red =(255,0,0)
green = (109,185,102)
sand = (242,225,174)

# dimensions
FIELD_X = 0.1 * display_width
FIELD_Y = 0.1 * display_height
FIELD_WIDTH = 0.8 * display_width
FIELD_HEIGHT = 0.8 * display_height

# player positions
PLAYER1_X = FIELD_X + 20
PLAYER2_X = FIELD_X + FIELD_WIDTH - 20
PLAYER_MIN_Y = FIELD_Y
PLAYER_MAX_Y = FIELD_Y + FIELD_HEIGHT

# ball initial position
BALL_INIT_X = FIELD_X + 30
BALL_INIT_Y = FIELD_Y + 50

# initializing pygame & creating window
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pynnis')
clock = pygame.time.Clock()

# sprites
all_sprites = pygame.sprite.Group()
field = Field(FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT, green)
player1 = Player(PLAYER1_X, PLAYER_MIN_Y, PLAYER_MAX_Y, red, pygame.K_a, pygame.K_s)
player2 = Player(PLAYER2_X, PLAYER_MIN_Y, PLAYER_MAX_Y, red, pygame.K_k, pygame.K_l)
ball = Ball(BALL_INIT_X, BALL_INIT_Y, black)
all_sprites.add(field)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)

quitted = False
# Creating game loop
while not quitted:
    # Speed of game loop defined by frames/second
    clock.tick(frames_per_second)
    # Input processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitted = True

    # Update of sprites (graphic elements)
    all_sprites.update()

    # Fill screen with color and draw sprites on it
    gameDisplay.fill(sand)
    all_sprites.draw(gameDisplay)
    pygame.display.update()

pygame.quit()
quit()
