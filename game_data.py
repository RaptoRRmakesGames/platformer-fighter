import pygame, pickle 
from pygame.locals import *

class LevelEditor:
    
    def __init__(self, collumns, rows, image_dict, screen, tile_size, bcg_color = (255,255,255)):
        self.collumns = collumns
        self.rows = rows 
        
        self.world_data = []
        
        for i in range(self.rows):
            
            self.world_data.append([-1] * self.collumns)
            
        self.images = image_dict
        
        self.screen = screen
        
        self.tile_size = tile_size
        
        self.bcg_color = bcg_color
            
    def draw_world(self, scroll):
        
        self.screen.fill(self.bcg_color)
        
        for y, row in enumerate(self.world_data):
            for x , tile in enumerate(row):
                
                if tile >= 0:
                    
                    self.screen.blit(self.images[tile], (x*self.tile_size - scroll[0], y*self.tile_size - scroll[1]))
                    
    def load_level(self, path):
        
        pickle_in = open(path, 'rb')
        self.world_data = pickle.load(pickle_in)
        pickle_in.close()
        
    def save_level(self, path):
        
        pi = open(path, 'wb')
        pickle.dump(self.world_data, pi)
        pi.close()
        
    def edit_tile(self, x, y, new_num):
        
        self.world_data[x][y] = new_num
   

class Game:
    
    def __init__(self, res, tile_size, collumn_rows, level_imgs, fps=0):
        
        self.screens = {
            "width" : res[0],
            "height" : res[1],
            "res" : res,
            'screen' : pygame.display.set_mode(res)
        }
        
        self.tiles = {
            "tile_size" : tile_size,
            "level" : LevelEditor(collumn_rows[0], collumn_rows[1], level_imgs, self.screens['screen'], tile_size)     
        }
        
        self.clocks = {
            "target_fps" : fps,
            "clock" : pygame.time.Clock(),
            "dt" : 1,
            "fps" : 0
        }
        
    def update_game(self):

        self.clocks['clock'].tick_busy_loop(self.clocks['target_fps'])
        
        self.clocks['fps'] = round(self.clocks['clock'].get_fps())
        
        
        # self.clocks['dt'] = self.clocks['clock'].tick() / 1000
        