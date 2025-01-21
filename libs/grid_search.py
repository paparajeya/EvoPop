import numpy as np
from typing import Dict
from .config import config

class GridSearch:
    def __init__(self, width=config.WIDTH, height=config.HEIGHT, grid_dim=config.GRID_SEARCH_DIM):
        self.width = width
        self.height = height
        self.grid_dim = grid_dim
        self.grid = self.__create_grid()
        self.grid_width = self.width // self.grid_dim[0]
        self.grid_height = self.height // self.grid_dim[1]
        
    def __create_grid(self):
        return np.empty(self.grid_dim, dtype=object)
    
    def add(self, pos, invidual_id: str):
        _x = pos.x // self.grid_width
        _y = pos.y // self.grid_height
        self.insert(_x, _y, invidual_id)
    
    def clear(self):
        self.grid = self.__create_grid()
        
    def get(self, x, y):
        return self.grid[x, y]
    
    def get_neighbors(self, x, y) -> Dict:
        neighbors = {}
        
        for i in range(-1, 2):
            for j in range(-1, 2):                
                _x = (x + i + self.grid_dim[0]) % self.grid_dim[0]
                _y = (y + j + self.grid_dim[1]) % self.grid_dim[1]
                
                neighbors[(_x, _y)] = self.grid[_x, _y]

        return neighbors
    
    def insert(self, x, y, invidual_id: str):
        if self.grid[x, y] is None:
            self.grid[x, y] = []
        self.grid[x, y].append(invidual_id)
        
    def move(self, x, y, new_x, new_y, invidual_id: str):
        self.remove(x, y, invidual_id)
        self.insert(new_x, new_y, invidual_id)
        
    def remove(self, x, y, invidual_id: str):
        self.grid[x, y].remove(invidual_id)
