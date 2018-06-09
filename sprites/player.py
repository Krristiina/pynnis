import pygame

class Player(pygame.sprite.Sprite):
    racket_height = 20
    racket_width = 30

    def __init__(self, init_x, init_y, color, down_key, up_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.racket_height, self.racket_width))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = init_x
        self.rect.bottom = init_y
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
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600


