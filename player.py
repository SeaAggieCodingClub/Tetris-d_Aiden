import pygame
import main

class Player:

    sprite = None
    rect = None
    speed = 1
    gravSpd = 0

    def __init__(self, imageString, playerSize):
        self.sprite = pygame.image.load(imageString)
        self.sprite = pygame.transform.scale(self.sprite, playerSize)

        self.rect = self.sprite.get_rect()

    def Update(self): #This method should be called every frame by main.py

        main.screen.blit(self.sprite, self.rect)

        oldPos = self.rect.center

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        for block in main.blocks:
            if block.rect.colliderect(self.rect):
                self.rect.center = oldPos

        oldPos = self.rect.center

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        for block in main.blocks:
            if block.rect.colliderect(self.rect):
                self.rect.center = oldPos

        oldPos = self.rect.center
        
        self.rect.y += self.gravSpd
        self.gravSpd += .01
        for block in main.blocks:
            if block.rect.colliderect(self.rect):
                self.rect.center = oldPos
                self.gravSpd = 0