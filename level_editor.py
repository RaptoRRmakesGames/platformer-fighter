import pygame ,pickle ,game_data
from assets import IMAGES
from pygame.locals import *


pygame.init()

run = True

level = 1

screen = pygame.display.set_mode((1000,800), RESIZABLE)

font = pygame.font.SysFont('roboto', 15)
font2 = pygame.font.SysFont('roboto', 45)

ground0 = pygame.image.load("images/ground/ground0.png")
ground1 = pygame.image.load("images/ground/ground1.png")

tile_map = game_data.LevelEditor(200, 16, IMAGES['ground'], screen, 50)

def draw_text(text, colour, font, pos, surface=screen):
    
    img = font.render(str(text), True, colour)
    
    surface.blit(img, pos)


def draw_grid(scroll, cords):
    
    for x in range(0, 1000, 50):
        
        for y in range(0,1000, 50):
            
            rect = pygame.Rect(x-scroll,y , 50,50)
            
            
            pygame.draw.rect(screen, (100,200,200), rect, 1)
            
            if cords:
            
                draw_text(f"x {x//50},", (200,200,200), font, (x + 10 - scroll,y +10), surface=screen)
                draw_text(f"y {y//50},", (200,200,200), font, (x + 10 - scroll,y + 30), surface=screen)
            
            


def move_grid():
    
    global scroll
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        
        if not scroll < 0:
        
            scroll -= 1
        
    if keys[pygame.K_RIGHT]:
        
        scroll += 1
        
    if keys[pygame.K_d]:
    
        scroll += 2
        
    if keys[K_a]:
        
        if not scroll < 0:
            scroll -= 2
            
def draw_ui(bgc=(215,255,171)):
    pygame.draw.rect(screen, bgc, pygame.Rect(700, 0, 300, 1000))
    pygame.draw.rect(screen, bgc, pygame.Rect(0, 700, 1000, 400))
    
sample_images = IMAGES['ground']

ui = draw_ui()

clock = pygame.time.Clock()

scroll = 0

try:

    tile_map.load_level(f"level{level}.lvl")
    
except FileNotFoundError:                
    tile_map.recreate_data()
    tile_map.save_level(f"level{level}.lvl")

mode = 0 

show_cords = True

while run:
    
    
    screen.fill((255,255,255))
    
    tile_map.draw_world((scroll,0))
    
    draw_grid(scroll, show_cords)
    
    selected_x = round((pygame.mouse.get_pos()[1] - 25)/50)
    selected_y = round((pygame.mouse.get_pos()[0] - 25 + scroll)/50)
    max_visible_x = int((700 -25 + scroll)//50) 
    
    if selected_x > max_visible_x:
        
        selected_x = max_visible_x
    
    
    
    draw_ui()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            run = False
            
        if event.type == MOUSEBUTTONDOWN:
            
            if event.button == 1:
            
                print(f"place x:{selected_x} y:{selected_y}")
            
                tile_map.world_data[selected_x][selected_y] = mode
                
            if event.button == 3:
                print(f"removed x:{selected_x} y:{selected_y}")
            
                tile_map.world_data[selected_x][selected_y] = -1
                
                
        if event.type == KEYDOWN:
            
            if event.key == K_x:
                
                show_cords = not show_cords
            
            if event.key == K_s:
                
                tile_map.save_level(f"level{level}.lvl")
                
                print('saved')
                
            if event.key == K_l:
                
                tile_map.load_level(f"level{level}.lvl")
                
            if event.key == K_UP:
                
                level += 1
                
                try:
                    tile_map.load_level(f"level{level}.lvl")
                except FileNotFoundError:
                    
                    tile_map.recreate_data()
                    tile_map.save_level(f"level{level}.lvl")
                
            if event.key == K_DOWN:
                
                if level != 1:
                
                    level -= 1
                
                    try:
                        tile_map.load_level(f"level{level}.lvl")
                    except FileNotFoundError:
                        
                        tile_map.recreate_data()
                        tile_map.save_level(f"level{level}.lvl")
                        
            
            if event.key == K_0 : 
                
                mode = 0 
                
            if event.key == K_1:
                
                mode = 1
                
            if event.key == K_2:
                
                mode = 2
                
            if event.key == K_3:
                
                mode = 3
                
            if event.key == K_4:
                
                mode = 4
                
            if event.key == K_5:
                
                mode = 5
                
    draw_text(f"Level : {level}", (0,0,0), font2, (20,700))
    screen.blit(sample_images[mode], (220, 710))
            
    move_grid()
    
    clock.tick_busy_loop(0)
        
    # print(selected_x, selected_y, max_visible_x)
            
    pygame.display.flip()
    
pygame.quit()