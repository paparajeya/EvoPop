import math
from enum import Enum

# Invividual Types - use enum MALE: 1 FEMALE: 0
class Gender(Enum):
    MALE = 1
    FEMALE = 0
    
class Strength(Enum):
    WEAK = 0
    NORMAL = 1
    STRONG = 2

class Config:
    WIDTH = 1800
    HEIGHT = 1000
    DEPTH = int(min(WIDTH, HEIGHT) / 10)
    FPS = 60
    CAPTION = "Evolution Simulator"
    BACKGROUND_COLOR = (255, 255, 255)
    GRID_SEARCH_DIM = [WIDTH//100, HEIGHT//100] #, DEPTH//20]
    
    # Population
    INIT_MALES = 75
    INIT_FEMALES = 75
    MAX_POPULATION = 5000
    MUTATION_RATE = 0.01
    CHOROMOSOME_LENGTH = 24
    GENDER_INDEX = CHOROMOSOME_LENGTH - 1
    MIN_CHROMOSOME_SHARED = math.floor(CHOROMOSOME_LENGTH * 0.3) # 30% of the chromosome must be shared. This must be less than CHOROMOSOME_LENGTH // 2
    
    # Weak, Normal, Strong
    OFFSPRING_STRENGTH_MATRIX = [
        [0.35, 0.6, 0.05],
        [0.25, 0.65, 0.1],
        [0.15, 0.55, 0.3]
    ]
    
    STRENGTH_RANGE = (0, CHOROMOSOME_LENGTH*0.4, CHOROMOSOME_LENGTH*0.75, CHOROMOSOME_LENGTH)
    STRENGTH_SIZE_INIT = {
        Strength.WEAK: 1,
        Strength.NORMAL: 2,
        Strength.STRONG: 3
    }
    STRENGTH_INTENSITY = {
        Strength.WEAK: [0, 0.5],
        Strength.NORMAL: [0.1, 0.75],
        Strength.STRONG: [0.25, 1]
    }
    
    LIFETIME_RANGE = {
        Strength.WEAK: [10, 15],
        Strength.NORMAL: [15, 20],
        Strength.STRONG: [20, 25]
    }
    
    # COLORS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PASTEL_CREAM = (255, 254, 224)
    PASTEL_BLOND = (255, 248, 213)
    PASTEL_AQUA = (213, 246, 251)
    PASTEL_LEMON = (246, 243, 169)
    PASTEL_SNOW = (229, 236, 248)
    PASTEL_PEARL = (240, 235, 216)
    
    
    # Simulation
    FONT = "Arial"
    FONT_SIZE = 20
    FONT_COLOR = (0, 0, 0)
    FONT_COLOR_HIGHLIGHT = (255, 0, 0)
    FONT_COLOR_DISABLED = (128, 128, 128)
    FONT_COLOR_SELECTED = (0, 0, 255)
    FONT_COLOR_SELECTED_HIGHLIGHT = (255, 0, 255)
    FONT_COLOR_SELECTED_DISABLED = (128, 128, 255)
    FONT_COLOR_TEXT = (0, 0, 0)
    FONT_COLOR_TEXT_HIGHLIGHT = (255, 0, 0)
    FONT_COLOR_TEXT_DISABLED = (128, 128, 128)
    FONT_COLOR_TEXT_SELECTED = (0, 0, 255)
    FONT_COLOR_TEXT_SELECTED_HIGHLIGHT = (255, 0, 255)
    FONT_COLOR_TEXT_SELECTED_DISABLED = (128, 128, 255)
    
    
config = Config()