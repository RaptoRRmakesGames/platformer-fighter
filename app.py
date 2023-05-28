import pygame, game_data, characters, enemies
from pygame.locals import *
from assets import IMAGES

game = game_data.Game((1000,700), 50, (0,0), IMAGES['ground'],140)

level = 1

run = True

game.tiles['level'].load_level(f"level{level}.lvl")

player = characters.Player((100,100))


enemy_list = [enemies.Enemy((100,400), "normal", True, 0, 200, 5, hp=10) for i in range(1)]

slomo = False

scroll_x = 0 

true_scroll = 0

while run: 
    game.update_game()
    
    # true_scroll -= 0.5
    #true_scroll +=( player.rect.x - true_scroll - 400) /5
    
    scroll_x = int(true_scroll)
    
    game.tiles['level'].draw_world((scroll_x,0))
    
    player.update(game.screens['screen'], game.tiles['level'].world_data, scroll_x)
    
    for enemy in enemy_list:
    
        enemy.update(game.screens['screen'], game.tiles['level'].world_data, player, player.shooter.bullets, enemy_list, scroll_x)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            run = False
            
            quit()
        
        if event.type == KEYDOWN:
            
            if event.key == K_f:
                
                slomo = not slomo 
                
    if slomo :
        
        game.clocks['target_fps'] = 25
        
    else: 
        game.clocks['target_fps'] = 140
            
    pygame.display.set_caption(str(game.clocks['fps']) + "FPS" )
            
    # print(game.clocks['fps'], "FPS")
            
    pygame.display.flip()
    
pygame.quit()