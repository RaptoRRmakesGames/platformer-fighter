import pygame, game_data, characters
from pygame.locals import *

black = pygame.Surface((50,50))

black.fill((0,0,0))

game = game_data.Game((600,600), 50, (16,16), {0: black},0)

level = 2

run = True

# game.tiles['level'].edit_tile(10,1, 0)
# game.tiles['level'].edit_tile(10,2, 0)
# game.tiles['level'].edit_tile(10,3, 0)
# game.tiles['level'].edit_tile(10,4, 0)
# game.tiles['level'].edit_tile(10,5, 0)
# game.tiles['level'].edit_tile(10,6, 0)
# game.tiles['level'].edit_tile(10,7, 0)
game.tiles['level'].load_level(f"level{level}.lvl")

player = characters.Player((100,100))

while run: 
    game.update_game()
    
    game.tiles['level'].draw_world((0,0))
    
    player.update(game.screens['screen'])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            game.tiles['level'].save_level(f"level{level}.lvl")
            
            run = False
            
            quit()
            
    # print(game.clocks['fps'])
            
    pygame.display.flip()