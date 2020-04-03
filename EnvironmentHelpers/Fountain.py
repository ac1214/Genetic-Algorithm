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
MAX_MOVES = 200

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
        self.screen.setup(width=SCREEN_WIDTH + 50, height=700)
        self.screen.bgcolor(SCREEN_COLOR)

        # Import all images into the screen
        self.screen.addshape(TILLY)
        self.screen.addshape(TILE_SHAPES[CRACKED_TILE])
        self.screen.addshape(TILE_SHAPES[REGULAR_TILE])
        self.tiles_dict = {}

        # Title
        title = turtle.Turtle()
        title.hideturtle()
        title.penup()
        title.color('black')
        style = ('Courier', 26)
        title.setpos(0, 300)
        title.write('CPSC-565: Assignment 3', font=style, align='center')
        style = ('Courier', 13)
        title.setpos(0, 280)
        title.write('By: James Peralta, Albert Choi, Nathaniel Habtegergesa',
                    font=style, align='center')

        # Create earning turtle
        self.earnings = turtle.Turtle()
        self.earnings.penup()
        self.earnings.hideturtle()
        self.earnings.speed(10)
        self.earnings.setpos(0, -300)

        # Create moves left turtle
        self.moves_left = turtle.Turtle()
        self.moves_left.penup()
        self.moves_left.hideturtle()
        self.moves_left.speed(10)
        self.moves_left.setpos(0, -340)

        # Create clearer turtle
        self.clearer = turtle.Turtle()
        self.clearer.penup()
        self.clearer.hideturtle()
        self.clearer.speed(10)
        self.clearer.setpos(0, -350)

        self.draw_earnings(0)
        self.draw_energy(0)

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

    def draw_earnings(self, earnings_val):
        style = ('Courier', 26)
        self.earnings.color('black')
        self.earnings.write('Earnings: {}'.format(
            earnings_val), font=style, align='center')

    def draw_energy(self, energy_val):
        style = ('Courier', 26)
        self.moves_left.color('black')
        self.moves_left.write('Energy left: {}'.format(
            MAX_MOVES - energy_val), font=style, align='center')

    def clear_board(self):
        self.clearer.setpos(-150, -250)
        self.clearer.fillcolor(SCREEN_COLOR)
        self.clearer.begin_fill()
        for i in range(4):
            self.clearer.forward(500)
            self.clearer.right(90)
        self.clearer.end_fill()
