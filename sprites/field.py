import pygame

class Field(pygame.sprite.Sprite):

    def __init__(self, dimensions, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((dimensions['FIELD_WIDTH'], dimensions['FIELD_HEIGHT']))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['X_POSITION_FIELD']
        self.rect.y = dimensions['Y_POSITION_FIELD']

    def update(self):
        pass
