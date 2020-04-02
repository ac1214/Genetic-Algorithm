# ga.py
# This is the genetic algortihm for tilly
# James Peralta, Albert Choi, Nathaniel Habtegergesa
# March 2020
import random
import copy
# import numpy as np
# import EnvironmentHelpers.

# Global Variables
mutationRate = 0.1
mutationRadius = 5
nGenerations = 500
rouletteFactor = 0.6
structures_per_generation = 1000


class Enviroment:
    # 0 - not broken
    # 1 - broken
    # 2 - falls off edge
    def __init__(self):
        self.generate_new_world()

    def generate_new_world(self):
        new_world = []
        for i in range(10):
            temp = []
            for j in range(10):
                temp.append(random.randint(0, 1))
            # print(temp)
            new_world.append(temp)

        self.world = copy.deepcopy(new_world)

    def getIndex(self, x, y, world):
        # print("x: ", x, " y: ", y)
        north = 2 if x == 0 else world[x - 1][y]
        east = 2 if y == 9 else world[x][y + 1]
        south = 2 if x == 9 else world[x + 1][y]
        west = 2 if y == 0 else world[x][y - 1]
        center = world[x][y]

        # [North, East, South, West, Below]

        temp = north * (3**4)
        temp += east * (3**3)
        temp += south * (3**2)
        temp += west * 3
        temp += center
        return temp

    def evaluate(self, struct):
        # iterate over 200 energy
        tempWorld = copy.deepcopy(self.world)

        x, y = 0, 0

        struct.earnings = 0
        # pheno = self.configure_phenotype(
        #     self.initalize_phenotype(), struct.genome)

        for i in range(200):
            # action = struct.phenotype(self.get_neighbors(x, y, tempWorld))
            action = struct.getMove(self.getIndex(x, y, tempWorld))
            # print(struct.genome)
            # print("x: ", x, " y: ",  y, " action ", action)
            # neigh = get_neighbors(x, y, tempWorld)
            # action = getAction(neigh)

            if action == 0:
                x -= 1
                if(x < 0):
                    struct.earnings -= 5  # remove magic numbers
                    x = 0
            elif action == 1:
                x += 1
                if(x > 9):
                    struct.earnings -= 5
                    x = 9
            elif action == 2:
                y -= 1
                if(y < 0):
                    struct.earnings -= 5
                    y = 0
            elif action == 3:
                y += 1
                if(y > 9):
                    struct.earnings -= 5
                    y = 9
            elif action == 4:
                if(tempWorld[x][y] == 0):
                    struct.earnings -= 1
                else:
                    tempWorld[x][y] = 0
                    struct.earnings += 10
            elif action == 5:
                pass
            else:
                choice = random.choice([True, False])
                if(choice):
                    choice = random.choice([True, False])
                    if(choice):
                        x -= 1
                        if(x < 0):
                            struct.earnings -= 5  # remove magic numbers
                            x = 0
                    else:
                        x += 1
                        if(x > 9):
                            struct.earnings -= 5
                            x = 9
                else:
                    choice = random.choice([True, False])
                    if(choice):
                        y -= 1
                        if(y < 0):
                            struct.earnings -= 5  # remove magic numbers
                            y = 0
                    else:
                        y += 1
                        if(y > 9):
                            struct.earnings -= 5
                            y = 9

            # print("action: ", action, "", "Earnings", struct.earnings)
        # print(moves)


class Structure:
    def __init__(self, actions):
        self.earnings = 0
        self.genome = actions[:]

        if(len(self.genome) == 0):
            self.genome = list()
            for i in range(243):
                self.genome.append(random.randint(0, 6))

    def getMove(self, index):
        return self.genome[index]

    def crossover(self, mate):
        childGenome = []

        crossoverPoint = random.randint(0, len(self.genome))
        for i in range(0, crossoverPoint):
            childGenome.append(self.genome[i])

        for i in range(crossoverPoint, len(self.genome)):
            childGenome.append(mate.genome[i])

        return Structure(childGenome)

    def mutate(self):
        for i in range(len(self.genome)):
            val = random.uniform(0, 1)
            if(val < mutationRate):
                radius = random.randint(-mutationRadius, mutationRadius)
                self.genome[i] = (self.genome[i] + radius) % 7


class GenePool:
    def __init__(self, structures, numStructs, world):
        self.pool = structures[:]
        self.poolSize = numStructs
        self.environment = world  # Create new world ?
        if self.pool == []:
            for _ in range(self.poolSize):
                self.pool.append(Structure([]))

        self.weights = [1]

        for i in range(1, self.poolSize):
            self.weights.append(self.weights[i - 1] * rouletteFactor)
        self.best = self.test()

    def selectStructures(self, num=2):
        return random.choices(self.pool, self.weights, k=num)

    def test(self):
        for struct in self.pool:
            self.environment.evaluate(struct)
        self.pool.sort(key=lambda x: x.earnings, reverse=True)
        # print(self.weights)
        # print([struct.earnings for struct in self.pool])

        return self.pool[0]

    def nextGen(self):
        newPool = []
        for _ in range(self.poolSize):
            parents = self.selectStructures(300)
            child = parents[0].crossover(parents[1])
            child.mutate()

            newPool.append(child)
        self.environment.generate_new_world()
        return GenePool(newPool, self.poolSize, self.environment)


def main():
    env = Enviroment()
    pool = GenePool([], structures_per_generation, env)
    for gen in range(nGenerations):
        print("Generation: ", gen, "  best earnings score: ", pool.best.earnings)
        print(pool.best.genome)
        pool = pool.nextGen()


main()
