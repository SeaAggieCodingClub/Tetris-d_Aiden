import pygame

WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
FPS = 60
SPRITE_SPEED = 5
DOG_SPRITE_SIZE = (50, 50)
BROWN = (165, 42, 42)

##

screen = pygame.display.set_mode((WIDTH, HEIGHT))
blocks = []
player = None

pygame.init()

pygame.display.set_caption("Epic Test")

clock = pygame.time.Clock()
running = True