import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, bounds):
        pygame.sprite.Sprite.__init__(self)
        self.bounds = bounds.image.get_rect()
        print (self.bounds.x)

        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 0, 255), (15, 15), 15)
        self.rect = self.image.get_rect()

        self.rect.center = (320, 240)

        self.dx = 5
        self.dy = 5

    def update(self):
        oldCenter = self.rect.center
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        self.checkBounds()

    def checkBounds(self):
        """ bounce on encountering any screen boundary """

        if self.rect.right >= self.bounds.right:
            self.dx *= -1
        if self.rect.left <= self.bounds.left:
            self.dx *= -1
        if self.rect.bottom >= self.bounds.bottom:
            self.dy *= -1
        if self.rect.top  <= self.bounds.top:
            self.dy *= -1