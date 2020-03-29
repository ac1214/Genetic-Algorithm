import turtle

# Constants
CRACKED_TILE = "./images/cracked_tile.gif"
REGULAR_TILE = "./images/regular_tile.gif"
TILE_BUILD_SPEED = 0


class Tile:
    def __init__(self, tile_type, x, y):
        if tile_type != REGULAR_TILE and tile_type != CRACKED_TILE:
            raise ValueError('Invalid tile type')

        if x is None or y is None:
            raise ValueError('Please set the coordinates')

        self.tile = turtle.Turtle()
        self.tile.penup()
        self.tile.speed(TILE_BUILD_SPEED)
        self.tile.shape(tile_type)
        self.tile.setpos((x, y))
