import pygame

# Selfmade Classes #

from player import Player
from block import Block

####################

blocks = []

pygame.init()

WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
FPS = 60
SPRITE_SPEED = 5
DOG_SPRITE_SIZE = (50, 50)
BROWN = (165, 42, 42)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epic Test")

clock = pygame.time.Clock()
running = True

player = Player("player.png", (50,50) )

blocks.append( Block( (50, 50), (100,100) ) )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    screen.blit(player.sprite, player.rect)

    oldPos = player.rect.center
    player.Update()

    for block in blocks:
        pygame.draw.rect(screen, BROWN, block.rect)

        if block.rect.colliderect(player.rect):
            player.rect.center = oldPos

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()