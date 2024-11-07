import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
FPS = 60
SPRITE_SPEED = 5
DOG_SPRITE_SIZE = (50, 50)
BROWN = (165, 42, 42)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog Sprite Movement")
dog_image = pygame.image.load('player.png')
dog_image = pygame.transform.scale(dog_image, DOG_SPRITE_SIZE) 
dog_rect = dog_image.get_rect()
dog_rect.topleft = (WIDTH // 2, HEIGHT // 2)

obstacles = [
    {'rect': pygame.Rect(100, 300, 100, 50), 'color': BROWN}, 
    {'rect': pygame.Rect(200, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(300, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(250, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(200, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(100, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(100, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(100, 220, 100, 50), 'color': BROWN}, 
    {'rect': pygame.Rect(0, 750, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(550, 250, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(100, 100, 100, 50), 'color': BROWN}, 
    {'rect': pygame.Rect(200, 0, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(300, 200, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(100, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(500, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(600, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(700, 300, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(300, 200, 100, 50), 'color': BROWN},  
    {'rect': pygame.Rect(300, 200, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(300, 200, 100, 50), 'color': BROWN},
    {'rect': pygame.Rect(0, HEIGHT - 50, 1000, 50), 'color': BROWN}
]

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dog_rect.x -= SPRITE_SPEED
    if keys[pygame.K_RIGHT]:
        dog_rect.x += SPRITE_SPEED
    if keys[pygame.K_UP]:
        dog_rect.y -= SPRITE_SPEED
    if keys[pygame.K_DOWN]:
        dog_rect.y += SPRITE_SPEED

    if dog_rect.left < 0:
        dog_rect.left = 0
    if dog_rect.right > WIDTH:
        dog_rect.right = WIDTH
    if dog_rect.top < 0:
        dog_rect.top = 0
    if dog_rect.bottom > HEIGHT:
        dog_rect.bottom = HEIGHT
    for obstacle in obstacles:
        if dog_rect.colliderect(obstacle['rect']):
            if keys[pygame.K_LEFT]:
                dog_rect.left = obstacle['rect'].right
            if keys[pygame.K_RIGHT]:
                dog_rect.right = obstacle['rect'].left
            if keys[pygame.K_UP]:
                dog_rect.top = obstacle['rect'].bottom
            if keys[pygame.K_DOWN]:
                dog_rect.bottom = obstacle['rect'].top


    screen.fill(BG_COLOR)
    screen.blit(dog_image, dog_rect)
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle['color'], obstacle['rect'])
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
