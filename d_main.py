# One Max Problem
from array import typecodes
from deap import tools
from deap import base, creator
import random
import array
import pdb

IND_SIZE = 5
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()


toolbox.register("individual", random.sample, range(IND_SIZE + 1), IND_SIZE)
toolbox.register("population", tools.initRepeat, creator.Individual, toolbox.individual)


if __name__ == "__main__":
    pop = toolbox.population(n=10)
