import pygame

class Block:

    sprite = None
    rect = None
    speed = 1

    def __init__(self, size, pos):
        #self.sprite = pygame.image.load(imageString)
        #self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        #self.rect = self.sprite.get_rect()

