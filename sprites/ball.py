import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, init_x, init_y, color, down_key, up_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.racket_height, self.racket_width))
        self.image.fill(color)
        self.rect = self.image.get_rect()