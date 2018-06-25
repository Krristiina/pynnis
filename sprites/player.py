import pygame

class Player(pygame.sprite.Sprite):
    racket_height = 50
    racket_width = 10

    def __init__(self, init_x, bounds_rect, color, down_key, up_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.racket_width, self.racket_height))
        self.image.fill(color)
        self.min_y = bounds_rect.top + self.racket_height
        self.max_y = bounds_rect.bottom - self.racket_height
        self.rect = self.image.get_rect()
        self.rect.centerx = init_x
        self.rect.centery = bounds_rect.top + (bounds_rect.bottom - bounds_rect.top) / 2
        self.down_key = down_key
        self.up_key = up_key
        self.speedy = 0

        #self.racket = pygame.rect.Rect(init_x, init_y, self.racket_width, self.racket_height)

    def update(self):
        # No movement unless certain keys are pressed
        self.speedy = 0
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.up_key]:
            self.speedy = -5
        if keys_pressed[self.down_key]:
            self.speedy = 5

        self.rect.y += self.speedy

        if self.rect.top > self.max_y:
            self.rect.top = self.max_y
        if self.rect.bottom < self.min_y:
            self.rect.bottom = self.min_y



