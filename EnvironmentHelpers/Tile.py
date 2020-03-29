import turtle

# Constants
CRACKED_TILE = "cracked"
REGULAR_TILE = "regular"
TILE_SHAPES = {"regular": "./images/regular_tile.gif", "cracked": "./images/cracked_tile.gif"}
TILE_BUILD_SPEED = 0


class Tile:
    """
    This class represents a single tile object in a fountain.
    """
    def __init__(self, tile_type, x, y):
        if tile_type not in TILE_SHAPES.keys():
            raise ValueError('Invalid tile type')

        if x is None or y is None:
            raise ValueError('Please set the coordinates')

        self.tile_type = tile_type
        self.tile = turtle.Turtle()
        self.tile.penup()
        self.tile.speed(TILE_BUILD_SPEED)
        self.tile.shape(TILE_SHAPES[tile_type])
        self.tile.setpos((x, y))

    def get_tile_type(self):
        return self.tile_type

    def set_tile_type(self, tile_type):
        self.tile_type = tile_type

    def fix_tile(self):
        self.set_tile_type(REGULAR_TILE)
        self.tile.shape(TILE_SHAPES[REGULAR_TILE])
