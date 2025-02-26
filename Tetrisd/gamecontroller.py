import pygame

# Selfmade Classes #

from player import Player
from block import Block
import main

####################





player = Player("player.png", (50,50) )

Block( (50, 50), (100,100) ) #Create block

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