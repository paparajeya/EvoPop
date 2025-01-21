import pygame

class Draw:
    
    @staticmethod
    def rect(screen, x, y, radius, color):
        pygame.draw.rect(screen, color, (x, y, radius, radius))
        
    @staticmethod
    def circle(screen, x, y, radius, color):
        pygame.draw.circle(screen, color, (x, y), radius)
        
    @staticmethod
    def triangle(screen, x, y, radius, color):
        pygame.draw.polygon(screen, color, [(x, y), (x + radius, y), (x + radius // 2, y - radius)])