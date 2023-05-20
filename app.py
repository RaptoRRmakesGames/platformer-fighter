import pygame, game_data, characters
from pygame.locals import *

black = pygame.Surface((50,50))

black.fill((0,0,0))

game = game_data.Game((600,600), 50, (14,14), {0: black},140)

level = 1

run = True

game.tiles['level'].edit_tile(10,0, 0)
game.tiles['level'].edit_tile(10,1, 0)
game.tiles['level'].edit_tile(10,2, 0)
game.tiles['level'].edit_tile(10,3, 0)
game.tiles['level'].edit_tile(10,4, 0)

game.tiles['level'].edit_tile(10,7, 0)
game.tiles['level'].edit_tile(9,7, 0)
game.tiles['level'].edit_tile(9,8, 0)
game.tiles['level'].edit_tile(11,10, 0)
game.tiles['level'].edit_tile(11,11, 0)
game.tiles['level'].edit_tile(10,11, 0)
game.tiles['level'].edit_tile(11,9, 0)
game.tiles['level'].edit_tile(11,8, 0)
game.tiles['level'].edit_tile(11,7, 0)
# game.tiles['level'].load_level(f"level{level}.lvl")

player = characters.Player((100,100))

while run: 
    game.update_game()
    
    game.tiles['level'].draw_world((0,0))
    
    player.update(game.screens['screen'], game.tiles['level'].world_data)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            game.tiles['level'].save_level(f"level{level}.lvl")
            
            run = False
            
            quit()
            
    # print(game.clocks['fps'], "FPS")
            
    pygame.display.flip()