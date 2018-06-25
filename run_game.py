#! /usr/bin/env python

import pygame
import random
from sprites.player import Player
from sprites.field import Field
from sprites.ball import Ball
from sprites.score import Score

#screen settings
display_width = 800
display_height = 600
frames_per_second = 60

#colors
black = (0,0,0)
red =(255,0,0)
green = (109,185,102)
sand = (242,225,174)
yellow = (220,249,0)
white = (255,255,255)

# dimensions
FIELD_X = 0.1 * display_width
FIELD_Y = 0.1 * display_height
FIELD_WIDTH = 0.8 * display_width
FIELD_HEIGHT = 0.8 * display_height

# player positions
PLAYER1_X = FIELD_X + 20
PLAYER2_X = FIELD_X + FIELD_WIDTH - 20

# initializing pygame & creating window
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
background = pygame.Surface(screen.get_size())
pygame.display.set_caption('Pynnis')
clock = pygame.time.Clock()

# sprites
all_sprites = pygame.sprite.Group()
field = Field(FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT, green)
player1 = Player(PLAYER1_X, field.rect, red, pygame.K_a, pygame.K_s)
player2 = Player(PLAYER2_X, field.rect, red, pygame.K_k, pygame.K_l)
ball = Ball(field.rect, yellow)
score = Score(FIELD_X + FIELD_WIDTH / 2 - 100, 5, 200, 50, 32, white, black)

all_sprites.add(field)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)
all_sprites.add(score)

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

    # Did player hit the ball?
    if ball.rect.colliderect(player1.rect):
        ball.dx *= -1
    if ball.rect.colliderect(player2.rect):
        ball.dx *= -1

    # Is goal?
    if ball.rect.left <= field.rect.left:
        ball.init_position()
        score.player2_score += 1
    elif ball.rect.right >= field.rect.right:
        ball.init_position()
        score.player1_score += 1

    # Fill screen with color and draw sprites on it
    screen.fill(sand)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
quit()
