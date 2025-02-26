import pygame

# Selfmade Classes #

from player import Player
from block import Block
import main

####################

player = Player("player1.png", (50,50) )

Block( (50, 50), (100,100) ) #Create block

Block( (main.WIDTH, main.HEIGHT), (-main.WIDTH, 0) )
Block( (main.WIDTH, main.HEIGHT), (0, -main.HEIGHT) )
Block( (main.WIDTH, main.HEIGHT), (main.WIDTH, 0) )
Block( (main.WIDTH, main.HEIGHT), (0, main.HEIGHT) )

while main.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.running = False

    main.screen.fill(main.BG_COLOR)

    player.Update()

    for block in main.blocks:

        block.Update()

    pygame.display.flip()
    main.clock.tick(main.FPS)

pygame.quit()