from .genetic import Genetic
from .config import config, Gender, Strength
from .individual import Individual
from .grid_search import GridSearch

class Population:
    def __init__(self):
        self.alive = {
            Gender.MALE: {
                Strength.WEAK: {},
                Strength.NORMAL: {},
                Strength.STRONG: {}
            },
            Gender.FEMALE: {
                Strength.WEAK: {},
                Strength.NORMAL: {},
                Strength.STRONG: {}
            }
        }
        self.dead = {
            Gender.MALE: {
                Strength.WEAK: {},
                Strength.NORMAL: {},
                Strength.STRONG: {}
            },
            Gender.FEMALE: {
                Strength.WEAK: {},
                Strength.NORMAL: {},
                Strength.STRONG: {}
            }
        }
        
        self.male_grid = GridSearch()
        self.female_grid = GridSearch()
        
        self.__init()
    
    def __init(self):
        # generate initial population
        people = Genetic.generate_chromosomes(Gender.MALE)
        people += Genetic.generate_chromosomes(Gender.FEMALE)
        
        for chromosome in people:
            gender = Gender.MALE if self.chromosome[config.GENDER_INDEX] else Gender.FEMALE
            _grid = self.male_grid if gender == Gender.MALE else self.female_grid
            individual = Individual(chromosome=chromosome, gender=gender, grid=_grid)
            self.alive[individual.gender][individual.strength][individual.id] = individual
        self.populate_grid()
        
    def draw(self, screen):
        for _, v in self.alive.items():
            for _, i in v.items():
                for _, individual in i.items():
                    individual.draw(screen)
                    
    def populate_grid(self):
        for _, v in self.alive.items():
            for _, i in v.items():
                for _, individual in i.items():
                    if individual.gender == Gender.MALE:
                        self.male_grid.add(individual.pos, individual.id)
                    else:
                        self.female_grid.add(individual.pos, individual.id) 
            
    def update(self):
        self