import pygame

class Ball(pygame.sprite.Sprite):
    
    arc = 8

    def __init__(self, init_x, init_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.arc * 2, self.arc * 2), pygame.SRCALPHA)
        self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.arc, self.arc), self.arc, 0)
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y

    def update(self):
        pass