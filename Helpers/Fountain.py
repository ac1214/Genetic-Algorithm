from Helpers.Tile import *
import random
import turtle

TILLY = "./images/tilly.gif"
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
TILES_PER_ROW = 10
TILES_PER_COL = 10
SCREEN_COLOR = "light green"


class Fountain:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_COLOR)

        # Import all images into the screen
        self.screen.addshape(TILLY)
        self.screen.addshape(CRACKED_TILE)
        self.screen.addshape(REGULAR_TILE)

    def generate_fountain(self):
        for x_coord in range(-int(SCREEN_WIDTH/2), int(SCREEN_WIDTH/2), int(SCREEN_WIDTH/TILES_PER_ROW)):
            for y_coord in range(-int(SCREEN_HEIGHT/2), int(SCREEN_HEIGHT/2), int(SCREEN_HEIGHT/TILES_PER_COL)):
                if random.uniform(0, 1) < 0.50:
                    Tile(REGULAR_TILE, x_coord, y_coord)
                    continue

                Tile(CRACKED_TILE, x_coord, y_coord)

