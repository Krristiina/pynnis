#! /usr/bin/env python

import pygame

#screen settings
display_width = 800
display_height = 600
frames_per_second = 60

#colors
black = (0,0,0)
white = (255, 255,255)
turquoise =(0,255,255)
red =(255,0,0)


#initializing pygame & creating window
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pynnis')
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    racket_height = 20
    racket_width = 30

    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.racket_height, self.racket_width))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = init_x
        self.rect.bottom = init_y

        #self.racket = pygame.rect.Rect(init_x, init_y, self.racket_width, self.racket_height)

    def update(self):
        self.rect.bottom = self.rect.bottom

all_sprites = pygame.sprite.Group()
player1 = Player(display_width / 4, display_height / 2)
player2 = Player((display_width / 4) * 3, display_height / 2)
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
    gameDisplay.fill(turquoise)
    all_sprites.draw(gameDisplay)
    pygame.display.update()


pygame.quit()
quit()


