import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect(pos[0], pos[1], 30,30)
        self.color = (0,0,0)
        
        self.speed = 3
        self.velocity = pygame.math.Vector2(0,0)
        self.next_x = 0
        self.next_y = 0
        
    def update(self, screen):
        
        pygame.draw.rect(screen, self.color, self.rect)
        
    def movement(self):
        
        keys = pygame.key.get_pressed()