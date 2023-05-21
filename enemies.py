import pygame, settings, characters
from pygame.locals import *
from random import randint, choice
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, id, shooting, least_x, max_x, damage, colour = (0,0,255), firerate=300) :
        pygame.sprite.Sprite.__init__(self)
        
        self.type = id 
        
        self.shooting = shooting
        self.damage = damage
        
        self.least_x = least_x
        self.max_x = max_x
        
        self.flip = False
        self.ori = 1 
        
        # STATES ARE 'PATROL' AND 'ATTACK' 
        self.state = "patrol"
        
        if self.shooting:
            
            self.shoot_controller = characters.ShootController(self, damage)
            
            self.fr = firerate
            self.next_shoot = pygame.time.get_ticks() + firerate
            
        self.rect = pygame.Rect(pos[0], pos[1], 40, 30)
        self.position = pygame.math.Vector2(self.rect.center)
        
        self.color = colour
        
    def shoot(self, player):
        
        if self.shooting and self.state == "attack":
            
            time_now = pygame.time.get_ticks()
            
            if time_now > self.next_shoot:
                
                if randint(1,3) == 1:
                    
                    random_x, random_y = randint(-20,20), randint(-20,20)
                    
                    self.shoot_controller.shoot((player.rect.center[0] + random_x, player.rect.center[1] + random_y))
                    
                self.next_shoot = time_now + self.fr
                    
    def detect_player(self, player, tiles, screen):
        player_pos = pygame.math.Vector2(player.rect.center)
        imaginary_pos = self.position
        imaginary_rect = pygame.Rect(imaginary_pos.x, imaginary_pos.y, 5, 5)
        e = 0
        
        rects, step = 2, 100
        
        while e < rects:
            imaginary_pos = imaginary_pos.move_towards(player_pos, step)
            imaginary_rect.topleft = imaginary_pos
            
            if player.rect.colliderect(imaginary_rect):
                return "attack"
            
            for y, row in enumerate(tiles):
                for x, tile in enumerate(row):
                    if tile > -1 and pygame.Rect(x*50, y*50, 50, 50).colliderect(imaginary_rect):
                        return "patrol"
            
            pygame.draw.rect(screen, (255, 255, 0), imaginary_rect)
            e += 1
        
        return "patrol"
        
                    
    def update(self, screen, tiles, player):
        self.position = pygame.math.Vector2(self.rect.center)
        
        self.state = self.detect_player(player, tiles, screen)
        
        self.shoot(player)
        
        self.shoot_controller.update_bullets(screen, tiles)
        
        
        pygame.draw.rect(screen,  self.color, self.rect)
        
        