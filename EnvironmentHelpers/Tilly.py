from EnvironmentHelpers.Fountain import *
import random

TILLY_SPEED = 0

state_to_int = {
    "regular": 0,
    "cracked": 1
}

BEST_ARRAY = [3, 4, 4, 2, 4, 0, 3, 4, 6, 1, 6, 0, 1, 4, 6, 1, 1, 2, 2, 4, 1, 2, 4, 6, 2, 3, 0, 3, 2, 4, 1, 3, 2, 6, 3, 3, 1, 1, 2, 1, 4, 1, 3, 6, 4, 0, 5, 2, 2, 2, 0, 2, 2, 4, 0, 4, 1, 2, 4, 0, 1, 5, 0, 5, 4, 2, 5, 1, 5, 2, 3, 1, 0, 2, 4, 4, 3, 0, 3, 4, 3, 0, 4, 5, 2, 4, 3, 5, 6, 6, 1, 4, 1, 3, 4, 0, 3, 3, 2, 6, 1, 5, 2, 4, 1, 0, 4, 3, 0, 1, 6, 1, 0, 3, 0, 1, 1, 6, 3,
              5, 3, 0, 6, 2, 5, 1, 6, 5, 3, 3, 0, 3, 4, 5, 0, 6, 4, 6, 4, 3, 2, 5, 2, 4, 5, 6, 3, 3, 1, 1, 3, 0, 6, 5, 3, 1, 0, 1, 4, 2, 0, 2, 2, 4, 1, 2, 6, 1, 6, 2, 1, 2, 3, 5, 6, 0, 4, 6, 6, 5, 3, 5, 3, 1, 4, 4, 2, 4, 6, 1, 4, 2, 2, 4, 5, 1, 6, 1, 1, 4, 2, 2, 0, 1, 3, 4, 4, 1, 5, 4, 6, 0, 4, 1, 0, 4, 6, 4, 4, 4, 2, 4, 2, 3, 5, 5, 6, 5, 6, 6, 0, 3, 1, 4, 6, 1, 5, 4, 0, 3, 0, 0, 1]

MOVE_UP = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_RIGHT = 3
MAKE_FIX = 4
DO_NOTHING = 5
MOVE_RANDOM = 6


class Tilly:
    """
    This class represents Tilly.
    """

    def __init__(self, fountain):
        self.tilly = turtle.Turtle()
        self.tilly.speed(TILLY_SPEED)
        self.tilly.penup()
        self.tilly.shape(TILLY)
        self.fountain = fountain
        self.current_x = 0
        self.current_y = 0

        # Tilly will now listen for events
        turtle.onkeypress(self.move_up, 'Up')
        turtle.onkeypress(self.move_down, 'Down')
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.fix_current_tile, 'f')
        turtle.onkeypress(self.get_nearest_neighbors, 'g')
        turtle.listen()

    # Getters/Setters
    def get_current_pos(self):
        current_pos = self.tilly.pos()
        return self.round_int(int(current_pos[0])), self.round_int(int(current_pos[1]))

    # Actions listeners
    # TODO: Track when it goes OOB and do a noop
    def spawn_tilly(self):
        self.tilly.setpos(TOP_LEFT)

    def move_up(self):
        self.current_x -= 1
        if(current_x < 0):
            # earnings -= 5
            pass
        else:
            self.tilly.setheading(90)
            self.tilly.forward(TILE_LENGTH)

    def move_down(self):
        self.current_x += 1
        self.tilly.setheading(270)
        self.tilly.forward(TILE_LENGTH)

    def move_left(self):
        self.tilly.setheading(180)
        self.tilly.forward(TILE_LENGTH)

    def move_right(self):
        self.tilly.setheading(0)
        self.tilly.forward(TILE_LENGTH)

    def fix_current_tile(self):
        current_x, current_y = self.get_current_pos()

        try:
            tile = self.fountain.get_tile(current_x, current_y)
        except KeyError as e:
            print("{} is out of the fountains bounds.".format(e))
            return

        tile_type = tile.get_tile_type()
        if tile_type is CRACKED_TILE:
            tile.fix_tile()

    def make_move(self):
        move_to_make = self.get_nearest_neighbors()

        # MOVE_UP = 0
        # MOVE_DOWN = 1
        # MOVE_LEFT = 2
        # MOVE_RIGHT = 3
        # MAKE_FIX = 4
        # DO_NOTHING = 5
        # MOVE_RANDOM = 6

        if move_to_make == MOVE_UP:
            self.move_up()
        elif move_to_make == MOVE_DOWN:
            self.move_down()
        elif move_to_make == MOVE_LEFT:
            self.move_left()
        elif move_to_make == MOVE_RIGHT:
            self.move_right()
        elif move_to_make == MAKE_FIX:
            self.fix_current_tile()
        elif move_to_make == DO_NOTHING:
            pass
        else:
            all_functions = [self.move_up, self.move_down,
                             self.move_left, self.move_right]
            rand_index = random.randint(0, 3)
            all_functions[rand_index]()

    def get_nearest_neighbors(self):
        """
        Returns an array of the nearest neighbors as strings (cracked, regular, OOB)

        :return: [North, East, South, West, Below]
        """
        current_x, current_y = self.get_current_pos()

        neighor_arr = []
        # North
        try:
            tile_type = self.fountain.get_tile(
                current_x, current_y + TILE_LENGTH).get_tile_type()
            north = state_to_int[tile_type]
        except KeyError as e:
            north = 2

        # East
        try:
            tile_type = self.fountain.get_tile(
                current_x + TILE_LENGTH, current_y).get_tile_type()
            east = state_to_int[tile_type]
        except KeyError as e:
            east = 2

        # South
        try:
            tile_type = self.fountain.get_tile(
                current_x, current_y - TILE_LENGTH).get_tile_type()
            south = state_to_int[tile_type]
        except KeyError as e:
            south = 2

        # West
        try:
            tile_type = self.fountain.get_tile(
                current_x - TILE_LENGTH, current_y).get_tile_type()
            west = state_to_int[tile_type]
        except KeyError as e:
            west = 2

        # Below
        try:
            tile_type = self.fountain.get_tile(
                current_x, current_y).get_tile_type()
            center = state_to_int[tile_type]
        except KeyError as e:
            center = 2

        temp = north * (3**4)
        temp += east * (3**3)
        temp += south * (3**2)
        temp += west * 3
        temp += center

        print("".join(map(str, [north, east, south, west, center])))
        return BEST_ARRAY[temp]

    def round_int(self, number, base=25):
        return base * round(number / base)
