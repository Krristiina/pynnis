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

dimensions = {
    'X_POSITION_FIELD' : (display_width - 0.8*display_width) / 2,
    'Y_POSITION_FIELD' : (display_height - 0.8*display_height) / 2,
    'FIELD_WIDTH' : display_width * 0.8,
    'FIELD_HEIGHT' : display_height * 0.8,
}

#initializing pygame & creating window
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pynnis')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
field = Field(dimensions, green)
player1 = Player(display_width / 4, display_height / 2, dimensions, red, pygame.K_a, pygame.K_s)
player2 = Player((display_width / 4) * 3, display_height / 2, dimensions, red, pygame.K_k, pygame.K_l)
all_sprites.add(field)
all_sprites.add(player1)
all_sprites.add(player2)


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
