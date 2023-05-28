import pygame 
import pickle 
from pygame.locals import *


pygame.init()

run = True

level = 0 

screen = pygame.display.set_mode((1000,1000), RESIZABLE)

font = pygame.font.SysFont('roboto', 10)

def draw_text(text, colour, font, pos, surface=screen):
    
    img = font.render(str(text), True, colour)
    
    surface.blit(img, pos)
    
    


def draw_grid():
    
    grid = pygame.Surface((10000,1000))
    
    for x in range(0, 10000, 50):
        
        for y in range(0,1000, 50):
            
            rect = pygame.Rect(x,y , 50,50)
            
            
            pygame.draw.rect(grid, (200,200,200), rect, 1)
            
            draw_text(f"x {x/50},", (200,200,200), font, (x + 10,y +10), surface=grid)
            draw_text(f"y {y/50},", (200,200,200), font, (x + 10,y + 30), surface=grid)
            
            
    return grid
    
grid = draw_grid()

scroll = 0

while run:
    
    screen.fill((255,255,255))
    
    screen.blit(grid, (-scroll,0))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            run = False
            
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        
        if not scroll < 0:
        
            scroll -= 1
        
    if keys[pygame.K_RIGHT]:
        
        scroll += 1
            
    pygame.display.flip()