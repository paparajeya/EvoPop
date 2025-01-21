import random
from .config import config, Gender, Strength
from .point import Point
from .util import Util
from .genetic import Genetic
from .draw import Draw

FUNC_DRAW = {
    Strength.WEAK: Draw.triangle,
    Strength.NORMAL: Draw.circle,
    Strength.STRONG: Draw.rect
}

class Individual:
    def __init__(self, **kwargs):
        self.id = Util.id_generator()
        self.age = 0
        self.chromosome = kwargs.get('chromosome', [])
        self.fitness = Genetic.fitness(self.chromosome)
        self.strength = Genetic.strength(self.fitness)
        self.gender = kwargs.get('gender', Gender.MALE if self.chromosome[config.GENDER_INDEX] else Gender.FEMALE)
        self.color = config.RED if self.gender == Gender.FEMALE else config.GREEN
        self.is_mutant = kwargs.get('is_mutant', False)
        self.size = config.STRENGTH_SIZE_INIT[self.strength]
        self.lifetime = random.randint(config.LIFETIME_RANGE[self.strength][0], config.LIFETIME_RANGE[self.strength][1])
        self.pos = kwargs.get('pos', self.get_random_position())

    def __str__(self):
        return f'Chromosome: {self.chromosome}, Fitness: {self.fitness}'
    
    def get_random_position(self) -> Point:
        _x = random.randint(2*self.size, config.WIDTH - 2*self.size)
        _y = random.randint(2*self.size, config.HEIGHT - 2*self.size)
        _z = random.randint(2*self.size, config.DEPTH - 2*self.size)
        return Point(_x, _y, _z)
    
    def draw(self, screen):
        FUNC_DRAW[self.strength](screen, self.pos.x, self.pos.y, self.size, self.color)
    
    def update(self):
        pass