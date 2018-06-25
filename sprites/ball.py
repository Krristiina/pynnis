import pygame
from random import randint
from random import choice

class Ball(pygame.sprite.Sprite):
    
    arc = 10
    speed = 5

    def __init__(self, bounds_rect, color):
        pygame.sprite.Sprite.__init__(self)
        self.bounds_rect = bounds_rect

        # Create transparent background for the surface
        self.image = pygame.Surface((self.arc * 2, self.arc * 2)).convert_alpha()
        self.image.fill((0, 0, 0, 0))

        # Draw the ball shape
        pygame.draw.circle(self.image, (0, 0, 255), (self.arc, self.arc), self.arc)
        self.rect = self.image.get_rect()

        # Initialize position for the ball
        self.init_position()

    def init_position(self):
        # Vertical position is random
        start_y = randint(self.bounds_rect.top + self.arc * 2, self.bounds_rect.bottom - self.arc * 2)

        # Ball movement starts from left or right side of the field
        if (choice([True, False])):
            self.rect.center = (self.bounds_rect.left + 100, start_y)
            self.dx = self.speed
        else:
            self.rect.center = (self.bounds_rect.right - 100, start_y)
            self.dx = -self.speed
        
        self.dy = randint(1,6)

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        self.checkBounds()

    def checkBounds(self):
        """ bounce on top and bottom of the field """
        if self.rect.bottom >= self.bounds_rect.bottom:
            self.dy *= -1
        if self.rect.top  <= self.bounds_rect.top:
            self.dy *= -1
