import pygame, settings
from pygame.locals import *
import math

class Bullet:
    
    def __init__(self,  shooter, target_pos):
        
        self.target_pos = target_pos
        
        self.shooter = shooter
        
        self.speed = settings.bullet_speed
        
        self.rect = pygame.Rect(self.shooter.owner.rect.center[0], self.shooter.owner.rect.center[1], 10,10)
        angle = math.atan2(target_pos[1]-self.rect.y, target_pos[0]-self.rect.x)
        self.vel_x = math.cos(angle) * self.speed
        self.vel_y = math.sin(angle) * self.speed
        
        self.to_be_removed = False
        
    def update(self, screen, tiles):
        
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        if not screen.get_rect(topleft=(0,0)).colliderect(self.rect):
            
            self.to_be_removed = True
            
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                
                if tile > -1:
                    
                    tilerect = pygame.Rect(x*50, y*50, 50,50)
                    
                    if tilerect.colliderect(self.rect):
                        
                        self.to_be_removed = True
        
        pygame.draw.rect(screen, (255,0,0), self.rect)
        

class ShootController:
    
    def __init__(self, owner, damage):
        
        self.owner = owner 
        
        self.damage = damage
        
        self.bullets = []
        
    def shoot(self, target_pos):
        
        self.bullets.append(Bullet(self, target_pos))
    
    def update_bullets(self, screen, tiles):
        
        for bullet in self.bullets:
            if bullet.to_be_removed:
                
                self.bullets.remove(bullet)
        
        for bullet in self.bullets:
            
            bullet.update(screen, tiles)
            
        # print(len(self.bullets))

        

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect(pos[0], pos[1], 30,30)
        self.color = (0,0,0)
        
        self.base_speed = 2
        self.speed = 2
        
        self.next_x = 0
        self.next_y = 0
        self.vel_y = 0
        self.on_ground = False
        
        self.shooter = ShootController(self, 2)
        self.shot_interval = 200
        self.next_shot = pygame.time.get_ticks() + self.shot_interval
        self.can_shoot = True
        
        self.double_jump = True
        
        self.released_space = False
        
    def update(self, screen, tiles):
        
        self.movement()
        
        self.collisions(tiles)
        
        self.handle_shooting()
        
        self.shooter.update_bullets(screen, tiles)
        
        self.rect.x += self.next_x
        self.rect.y += self.next_y
        
        pygame.draw.rect(screen, self.color, self.rect)
        
    def handle_shooting(self):
        
        self.can_shoot = pygame.time.get_ticks() > self.next_shot
        
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            
            self.shooter.shoot(pygame.mouse.get_pos())
            
            self.next_shot = pygame.time.get_ticks() + self.shot_interval
            
        
            
        
    def movement(self):
        
        keys = pygame.key.get_pressed()
        
        self.next_x = 0
        
        if keys[K_LSHIFT]: # Sprinting
            
            if self.on_ground:
            
                self.speed = self.base_speed * 1.4

        else:
            
            self.speed = 2
        
        if keys[K_LCTRL]: # Crouching
            
            self.rect.height = 20
            self.speed = self.base_speed * 0.5
            
        else:
            
            self.rect.height = 30
        
        
        if keys[K_a]: # Moving Left
            
            self.next_x = -self.speed
            
        if keys[K_d]: # Moving Right
            
            self.next_x = self.speed
            
        if keys[K_SPACE] and self.on_ground: # Jumping
            
            self.on_ground = False
            
            self.vel_y = -7
            
        if not keys[K_SPACE] and not self.on_ground:
            
            self.released_space = True
        
        print(self.released_space)
            
            
        if keys[K_SPACE] and self.double_jump and not self.on_ground and self.vel_y > -2:
            
            self.double_jump = False
            
            self.vel_y = -6.5
            
        
        self.vel_y += settings.G
        
            
        self.next_y = self.vel_y
        
    def collisions(self, tiles):
        
       
        
        for y, row in enumerate(tiles):
            
            for x, tile in enumerate(row):
                
                if tile > -1:
                    
                    tilerect = pygame.Rect(x*50, y*50, 50,50)
                    
                    if tilerect.colliderect(self.rect.x + self.next_x, self.rect.y, self.rect.width, self.rect.height):
                        self.next_x = 0 
                        
                    if tilerect.colliderect(self.rect.x, self.rect.y + self.next_y, self.rect.width, self.rect.height):
                        
                        if self.vel_y < 0.0:
                            self.vel_y = 0 
                            self.next_y = tilerect.bottom - self.rect.top
                        
                        elif self.vel_y >= 0.0:
                            self.vel_y = 0 
                            self.on_ground = True
                            self.double_jump = True
                            self.next_y = tilerect.top - self.rect.bottom
                            
                            
        # print(self.on_ground, self.vel_y, self.next_y)
                    
            
        
        
        
        
        
        
        
        
            