import pygame, game_data, characters, enemies
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


enemy_list = [enemies.Enemy((200,400), "normal", True, 0, 400, 5) for i in range(2)]
# enemy = enemies.Enemy((50,400), "normal", True, 0, 100, 5)

slomo = False

while run: 
    game.update_game()
    
    game.tiles['level'].draw_world((0,0))
    
    player.update(game.screens['screen'], game.tiles['level'].world_data)
    
    for enemy in enemy_list:
    
        enemy.update(game.screens['screen'], game.tiles['level'].world_data, player)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            game.tiles['level'].save_level(f"level{level}.lvl")
            
            run = False
            
            quit()
        
        if event.type == KEYDOWN:
            
            if event.key == K_f:
                
                slomo = not slomo 
                
    if slomo :
        
        game.clocks['target_fps'] = 60
        
    else: 
        game.clocks['target_fps'] = 140

            
    # keys = pygame.key.get_pressed()
    
    # if keys[K_f]:
        
    #     game.clocks['target_fps'] = 60
    
    # else: 

    #     game.clocks['target_fps'] = 140
            
    pygame.display.set_caption(str(game.clocks['fps']) + "FPS" )
            
    # print(game.clocks['fps'], "FPS")
            
    pygame.display.flip()