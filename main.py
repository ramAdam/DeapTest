import array
import random

import numpy

from deap import algorithms, base, creator, tools
from util import allDuplicates, occurence
import pdb


I_LEN = 5
MAX_LOC = 10
lookup = {
    1: random.randint(0, MAX_LOC),
    2: random.randint(0, MAX_LOC),
    3: random.randint(0, MAX_LOC),
    4: random.randint(0, MAX_LOC),
    5: random.randint(0, MAX_LOC),
}

creator.create("FitnessMaxMin", base.Fitness, weights=(1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMaxMin)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("rand_int", random.randint, 0, I_LEN)

# Structure initializers
toolbox.register(
    "individual", tools.initRepeat, creator.Individual, toolbox.rand_int, I_LEN
)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# pdb.set_trace()


def evalDeapTest(individual):
    loc = []

    for e in individual:
        try:
            loc.append(lookup[e])
        except KeyError:
            loc.append(0)
    nTests = len(individual) - len(list(occurence(0, individual)))
    nLoc = sum(loc)

    return nLoc, nTests


def evalOneMax(individual):
    return (sum(individual),)


toolbox.register("evaluate", evalDeapTest)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():

    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)

    def getBestIndividual(self):
        return hof.items[0]

    def getScore(self):
        return hof.keys[0]

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    stats.register("fit Individual", getBestIndividual)

    pop, log = algorithms.eaSimple(
        pop,
        toolbox,
        cxpb=0.5,
        mutpb=0.2,
        ngen=40,
        stats=stats,
        halloffame=hof,
        verbose=True,
    )

    return pop, log, hof


if __name__ == "__main__":
    pop, log, hof = main()
    pdb.set_trace()
    # print(pop)