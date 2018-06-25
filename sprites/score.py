import pygame

class Score(pygame.sprite.Sprite):
  
  player1_score = 0
  player2_score = 0

  def __init__(self, x, y, width, height, font_size, board_color, text_color):
    pygame.sprite.Sprite.__init__(self)

    self.width = width
    self.height = height
    self.font_size = font_size
    self.board_color = board_color
    self.text_color = text_color

    self.image = pygame.Surface((self.width, self.height))

    self.rect = self.image.get_rect()
    self.rect.x = x;
    self.rect.y = y;

    self.update()

  def update(self):
    
    font = pygame.font.Font(None, self.font_size)
    text_surface = font.render(str(self.player1_score) + " – " + str(self.player2_score), True, self.text_color)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()

    self.image.fill(self.board_color)
    
    # centers text on sprite
    self.image.blit(text_surface, [self.width / 2 - text_width / 2, self.height / 2 - text_height / 2])
    
    pass