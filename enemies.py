import pygame, settings, characters
from pygame.locals import *
from random import randint, choice
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, id, shooting, least_x, max_x, damage, colour = (0,0,255), firerate=300, speed=2, hp = 1) :
        pygame.sprite.Sprite.__init__(self)
        
        self.type = id 
        
        self.shooting = shooting
        self.damage = damage
        
        self.speed = speed
        
        self.least_x = least_x
        self.max_x = max_x
        
        self.flip = False
        self.ori = -1 
        
        # STATES ARE 'PATROL' AND 'ATTACK' 
        self.state = "patrol"
        
        if self.shooting:
            
            self.shoot_controller = characters.ShootController(self, damage)
            
            self.fr = firerate
            self.next_shoot = pygame.time.get_ticks() + firerate
            
        self.rect = pygame.Rect(pos[0], pos[1], 40, 30)
        self.position = pygame.math.Vector2(self.rect.center)
        
        self.color = colour
        
        self.vel_y = 0
        self.next_y = 0
        self.next_x = 0 
        
        self.should_stop = False
        self.might_stop_interval = 1000
        self.next_might_stop = pygame.time.get_ticks() + self.might_stop_interval
        self.start_move_interval = 500
        self.next_start_move = pygame.time.get_ticks()
        
        self.hp = hp
        
        self.x = pos[0]
        
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
        
        rects, step = 7, 40
        
        while e < rects:
            imaginary_pos = imaginary_pos.move_towards(player_pos, step)
            imaginary_rect.topleft = imaginary_pos
            
            if player.rect.colliderect(imaginary_rect):
                return "attack"
            
            for y, row in enumerate(tiles):
                for x, tile in enumerate(row):
                    if tile > -1 and pygame.Rect(x*50, y*50, 50, 50).colliderect(imaginary_rect):
                        return "patrol"
            
            pygame.draw.rect(screen, (255, 0, 255), imaginary_rect)
            e += 1
        
        return "patrol"
    
    def collisions(self, tiles, scroll):
        
        for y , row in enumerate(tiles):
            for x, tile in enumerate(row):
                
                if tile > -1:
                    
                    tilerect = pygame.Rect(x*50 - scroll, y*50, 50,50)
                    
                    # if tilerect.colliderect(self.rect.x + self.next_x, self.rect.y, self.rect.width, self.rect.height):
                    #     self.flip = not self.flip
                    #     self.ori *=-1 
                        
                    if tilerect.colliderect(self.rect.x - scroll, self.rect.y + self.next_y, self.rect.width, self.rect.height):
    
                        if self.vel_y >= 0.0:
                            self.vel_y = 0 
                            self.next_y = tilerect.top - self.rect.bottom
                            
    def check_dead(self, bullets, enemy_list):
        
        for bullet in bullets:
            
            if self.rect.colliderect(bullet.rect):
                
                bullet.to_be_removed = True
                
                # print("shot")
                
                self.hp -= 1
                
        if self.hp < 1:
            
            
            # drop coins 
            
            enemy_list.remove(self)
            
            
            
        
        
                            
    def move(self, player):
        

            
        self.next_x = self.speed * self.ori
        
        if self.rect.x > self.max_x:
        
            self.ori = -1
            
            
        if self.rect.x < self.least_x:
            
            self.ori = 1
            
        if self.state == 'attack' and not self.should_stop:
            
            time_now = pygame.time.get_ticks()
            
        #     if time_now > self.next_might_stop:
            
        #         e = randint(1,5)
                
        #         if e == 3:
                    
        #             self.should_stop = True
                    
                
                
        #         self.next_start_move = pygame.time.get_ticks() + self.start_move_interval + randint(-100,100)
                
        
                    
                    
                
        # if self.should_stop:
            
        #     if pygame.time.get_ticks() > self.next_start_move:
                
        #         self.next_might_stop = pygame.time.get_ticks() + self.might_stop_interval
                
        #         self.should_stop = False
                
                
            
        #         self.ori = 0 
                
        self.vel_y += settings.G
        
        self.next_y = self.vel_y
                    
    def update(self, screen, tiles, player, bullets, enemy_list, scroll):
        self.position = pygame.math.Vector2(self.rect.center)
        
        self.state = self.detect_player(player, tiles, screen)
        
        self.shoot(player)
        
        self.move(player)
        self.collisions(tiles, scroll)
        
        self.check_dead(bullets, enemy_list)
        
        self.x += self.next_x
        self.rect.y += self.next_y
        
        self.rect.x = self.x - scroll
        
        self.shoot_controller.update_bullets(screen, tiles)
        
        pygame.draw.rect(screen,  self.color, pygame.Rect(self.rect.x - scroll, self.rect.y, 40,30))
        
        # print(self.least_x, self.max_x, self.rect.x, self.ori, self.state)
        # print(pygame.time.get_ticks(), self.should_stop, self.next_start_move, self.next_might_stop)
        
        