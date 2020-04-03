# ga.py
# This is the genetic algortihm for Tilly
# James Peralta, Albert Choi, Nathaniel Habtegergesa
# March 2020
import random
import copy

# Global Variables
mutation_rate = 0.05
mutation_radius = 5
roulette_factor = 0.8
n_generations = 1000
structures_per_generation = 500

MAX_ENERGY = 200
GENOME_LENGTH = 243

# State configurations
UNBROKEN = 0
BROKEN = 1
OOB = 2  # out of bounds

# Money to be earned
ONE_DOLLAR = 1
FIVE_DOLLARS = 5
TEN_DOLLARS = 10

# Edges in the map
TOP_EDGE = 0
BOTTOM_EDGE = 9
LEFT_EDGE = 0
RIGHT_EDGE = 9

# Actions
MOVE_UP = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_RIGHT = 3
MAKE_FIX = 4
DO_NOTHING = 5
MOVE_RANDOM = 6


class Environment:
    def __init__(self):
        self.world = self.generate_new_world()

    def generate_new_world(self):
        new_world = []
        for i in range(10):
            temp = []
            for j in range(10):
                temp.append(random.randint(0, 1))
            new_world.append(temp)

        return new_world

    def get_index(self, x, y, world):
        north = OOB if x == TOP_EDGE else world[x - 1][y]
        east = OOB if y == RIGHT_EDGE else world[x][y + 1]
        south = OOB if x == BOTTOM_EDGE else world[x + 1][y]
        west = OOB if y == LEFT_EDGE else world[x][y - 1]
        center = world[x][y]

        # [North, East, South, West, Below]
        #  Generates a bit string containing the index of
        #  the action in the genome depending on the current
        #  state of this structures neighbors
        state = north * (3**4)
        state += east * (3**3)
        state += south * (3**2)
        state += west * 3
        state += center
        return state  # Number between 0 and 242

    def evaluate(self, struct):
        row, col = 0, 0

        average_earnings = []
        # Evaluate on 10 different fountains
        for i in range(0, 5):
            earnings = 0
            temp_world = copy.deepcopy(self.generate_new_world())
            for i in range(MAX_ENERGY):
                action = struct.get_move(self.get_index(row, col, temp_world))

                if action == MOVE_UP:
                    row -= 1
                    # If Tilly falls off of the top edge
                    if row < TOP_EDGE:
                        earnings -= FIVE_DOLLARS
                        row = TOP_EDGE  # Place back on the top edge
                elif action == MOVE_DOWN:
                    row += 1
                    # If Tilly falls off of the bottom edge
                    if row > BOTTOM_EDGE:
                        earnings -= FIVE_DOLLARS
                        row = BOTTOM_EDGE  # Place back on the bottom edge
                elif action == MOVE_LEFT:
                    col -= 1
                    # If Tilly falls off of the left edge
                    if col < LEFT_EDGE:
                        earnings -= FIVE_DOLLARS
                        col = LEFT_EDGE  # Place back on the left edge
                elif action == MOVE_RIGHT:
                    col += 1
                    # If Tilly falls off of the right edge
                    if col > RIGHT_EDGE:
                        earnings -= FIVE_DOLLARS
                        col = RIGHT_EDGE  # Place back on the right edge
                elif action == MAKE_FIX:
                    # If tilly attempts to fix a tile that isn't broken
                    if(temp_world[row][col] == UNBROKEN):
                        earnings -= ONE_DOLLAR
                    else:
                        temp_world[row][col] = UNBROKEN
                        earnings += TEN_DOLLARS
                elif action == DO_NOTHING:
                    pass
                else:
                    choice = random.choice([True, False])
                    if choice:
                        choice = random.choice([True, False])
                        if choice:
                            row -= 1
                            if row < TOP_EDGE:
                                earnings -= FIVE_DOLLARS
                                row = TOP_EDGE
                        else:
                            row += 1
                            if row > BOTTOM_EDGE:
                                earnings -= FIVE_DOLLARS
                                row = BOTTOM_EDGE
                    else:
                        choice = random.choice([True, False])
                        if choice:
                            col -= 1
                            if(col < LEFT_EDGE):
                                earnings -= FIVE_DOLLARS
                                col = LEFT_EDGE
                        else:
                            col += 1
                            if(col > RIGHT_EDGE):
                                earnings -= FIVE_DOLLARS
                                col = RIGHT_EDGE

            average_earnings.append(earnings)
        # print(average_earnings)

        struct.earnings = sum(average_earnings) / len(average_earnings)


class Structure:
    def __init__(self, actions):
        self.earnings = 0
        self.genome = actions[:]

        if(self.genome == []):
            self.genome = list()
            for i in range(GENOME_LENGTH):
                self.genome.append(random.randint(0, 6))

    def get_move(self, index):
        return self.genome[index]

    def crossover(self, mate):
        child_genome = []

        for i in range(0, len(self.genome)):
            choice = random.choice([True, False])
            if(choice):
                child_genome.append(self.genome[i])
            else:
                child_genome.append(mate.genome[i])

        # Might implement two point crossover here
        # crossover_point = random.randint(0, len(self.genome))
        # for i in range(0, crossover_point):
        #     child_genome.append(self.genome[i])

        # for i in range(crossover_point, len(self.genome)):
        #     child_genome.append(mate.genome[i])

        return Structure(child_genome)

    def n_point_crossover(self, mate, n=2):
        child_genome = []
        crossover_points = random.sample(range(0, GENOME_LENGTH), n)
        crossover_points.sort()

        on_parent = True
        crossover_index = 0
        for i in range(0, GENOME_LENGTH):
            if i == crossover_points[crossover_index]:
                crossover_index = (crossover_index + 1) % len(crossover_points)
                on_parent = not on_parent

            if on_parent:
                child_genome.append(self.genome[i])
            else:
                child_genome.append(mate.genome[i])

        return Structure(child_genome)

    def mutate(self):
        for i in range(0, GENOME_LENGTH):
            val = random.uniform(0, 1)

            if val < mutation_rate:
                self.genome[i] = random.choice([0, 1, 2, 3, 4, 5, 6])

                # mutation = random.randint(1, mutation_radius)

                # choice = random.choice([True, False])
                # if(choice):
                #     self.genome[i] = (self.genome[i] + mutation) % 7
                # else:
                #     self.genome[i] = (self.genome[i] - mutation) % 7

                # new_point = random.randint(
                #     current_value - mutation_radius, current_value + mutation_radius)

                # if new_point < 0:
                #     self.genome[i] = 0
                # elif new_point > 6:
                #     self.genome[i] = 6
                # else:
                #     self.genome[i] = new_point


class GenePool:
    def __init__(self, structures, num_structs, world):
        self.pool = structures[:]
        self.pool_size = num_structs
        self.environment = world

        # Initialize pool to contain random Genomes
        if self.pool == []:
            for _ in range(self.pool_size):
                self.pool.append(Structure([]))

        # Generate probabilities for picking Genomes
        self.weights = [1]
        for i in range(1, self.pool_size):
            self.weights.append(self.weights[i - 1] * roulette_factor)

        self.best = self.test()

    def select_structures(self, num=2):
        return random.choices(self.pool, self.weights, k=num)

    def test(self):
        for struct in self.pool:
            self.environment.evaluate(struct)
        self.pool.sort(key=lambda x: x.earnings, reverse=True)

        return self.pool[0]

    def next_gen(self):
        scores = []
        new_pool = []
        for _ in range(self.pool_size):
            parents = self.select_structures()
            parent_zero = copy.deepcopy(parents[0])
            parent_one = copy.deepcopy(parents[1])
            child = parent_zero.n_point_crossover(parent_one, 1)
            child.mutate()

            scores.append(parent_zero.earnings)
            new_pool.append(child)

        new_env = Environment()
        return GenePool(new_pool, self.pool_size, new_env)


def main():
    env = Environment()
    pool = GenePool([], structures_per_generation, env)
    for gen in range(n_generations):
        print("Generation: ", gen, "  best earnings score: ", pool.best.earnings)
        pool = pool.next_gen()

    file_name = "generation_" + \
        str(n_generations) + "_fitness_score_" + \
        str(pool.best.earnings) + ".txt"

    #file = open(file_name, "w")
    array = " ".join(map(str, pool.best.genome))
    # file.write(array)
    # file.close()


main()
