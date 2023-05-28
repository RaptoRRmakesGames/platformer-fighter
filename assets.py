import pygame 

IMAGES = {
    
    "ground" : { 
        0 : pygame.image.load("images/ground/ground0.png"),
        1 : pygame.image.load("images/ground/ground1.png"),
        2 : pygame.image.load("images/ground/ground2.png"),
        3 : pygame.transform.flip(pygame.image.load("images/ground/ground2.png"),True, False),
        }
}