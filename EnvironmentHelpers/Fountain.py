from EnvironmentHelpers.Tile import *
import random
import turtle

# Constants
TILLY = "./images/tilly.gif"
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
TILES_PER_ROW = 10
TILES_PER_COL = 10
SCREEN_COLOR = "light green"
TILE_LENGTH = 50
TILE_OFFSET = 25
CRACKED_PERCENTAGE = 0.50

# Derived constants
TOP_LEFT = (-int(SCREEN_WIDTH/2) + TILE_OFFSET,
            int(SCREEN_HEIGHT/2) - TILE_OFFSET)
TOP_RIGHT = (int(SCREEN_WIDTH/2) - TILE_OFFSET,
             int(SCREEN_HEIGHT/2) - TILE_OFFSET)
BOTTOM_LEFT = (-int(SCREEN_WIDTH/2) + TILE_OFFSET, -
               int(SCREEN_HEIGHT/2) + TILE_OFFSET)
BOTTOM_RIGHT = (int(SCREEN_WIDTH/2) - TILE_OFFSET, -
                int(SCREEN_HEIGHT/2) + TILE_OFFSET)


class Fountain:
    """
    This class represents a fountain in a screen.

    Depending on the tiles per row and tiles per column:
    tiles_per_row X tiles_per_col =  # of tile objects.
    """

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_COLOR)

        # Import all images into the screen
        self.screen.addshape(TILLY)
        self.screen.addshape(TILE_SHAPES[CRACKED_TILE])
        self.screen.addshape(TILE_SHAPES[REGULAR_TILE])
        self.tiles_dict = {}

    def generate_fountain(self):
        for x_coord in range(TOP_LEFT[0], TOP_RIGHT[0] + TILE_OFFSET, int(SCREEN_WIDTH/TILES_PER_ROW)):
            for y_coord in range(BOTTOM_LEFT[1], TOP_LEFT[1] + TILE_OFFSET, int(SCREEN_HEIGHT/TILES_PER_COL)):
                tile_type = self.create_random_tile()
                self.tiles_dict[self.coord_to_string(x_coord, y_coord)] = Tile(
                    tile_type, x_coord, y_coord)

    def create_random_tile(self):
        if random.uniform(0, 1) < CRACKED_PERCENTAGE:
            return REGULAR_TILE

        return CRACKED_TILE

    def get_tile(self, x, y):
        return self.tiles_dict[self.coord_to_string(x, y)]

    def coord_to_string(self, x, y):
        return "({}, {})".format(x, y)
