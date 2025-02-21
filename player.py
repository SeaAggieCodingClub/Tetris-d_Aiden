import pygame

class Player:

    sprite = None
    rect = None
    speed = 1

    def __init__(self, imageString, playerSize):
        self.sprite = pygame.image.load(imageString)
        self.sprite = pygame.transform.scale(self.sprite, playerSize)

        self.rect = self.sprite.get_rect()

    def Update(self): #This method should be called every frame by main.py
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed