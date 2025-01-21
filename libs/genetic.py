import random
from typing import List, Literal
from .config import config, Gender, Strength

class Genetic:  
      
    @staticmethod
    def crossover(parent1, parent2, num_offspring: int=2, num_crossover: int=1) -> List[List[int]]:
        chromosome1 = parent1.chromosome
        chromosome2 = parent2.chromosome
        offsprings = []
        for _ in range(num_offspring):
            crossover_point = random.randint(config.MIN_CHROMOSOME_SHARED, len(chromosome1) - config.MIN_CHROMOSOME_SHARED)
            # generate a binary random number to determine which parent to select first
            if random.randint(0, 1) == 0:
                offsprings.append(chromosome1[:crossover_point] + chromosome2[crossover_point:])
            else:
                offsprings.append(chromosome2[:crossover_point] + chromosome1[crossover_point:])
        return offsprings
    
    @staticmethod
    def fitness(chromosome):
        return sum(chromosome)
    
    @staticmethod
    def generate_chromosomes(individual_type = Gender.MALE) -> List[List[int]]:
        chromosomes = []
        length = config.CHOROMOSOME_LENGTH
        # generate a random chromosome with 12 1's and 12 0's randomly placed
        chromosome = [1] * (length - 1)
        zero_length, total = (length // 2, config.INIT_MALES) if individual_type == Gender.MALE else ((length // 2) - 1, config.INIT_FEMALES)
           
        for _ in range(zero_length):
            p = random.randint(0, length - 2)
            while chromosome[p] == 0:
                p = random.randint(0, length - 2)
            chromosome[p] = 0
            
        for _ in range(total):
            _ch = chromosome.copy()
            _ch.append(individual_type.value)
            chromosomes.append(_ch)
            random.shuffle(chromosome)
        
        return chromosomes
    
    @staticmethod
    def strength(power) -> str:
        if power < config.STRENGTH_RANGE[1]:
            return Strength.WEAK
        elif power < config.STRENGTH_RANGE[2]:
            return Strength.NORMAL
        else:
            return Strength.STRONG 