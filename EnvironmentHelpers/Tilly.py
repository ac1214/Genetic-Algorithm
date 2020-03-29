from EnvironmentHelpers.Fountain import *

TILLY_SPEED = 0


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
        turtle.listen()

    # Getters/Setters
    def get_current_pos(self):
        current_pos = self.tilly.pos()
        return self.round_int(int(current_pos[0])), self.round_int(int(current_pos[1]))

    # Actions listeners
    def spawn_tilly(self):
        self.tilly.setpos(TOP_LEFT)

    def move_up(self):
        self.tilly.setheading(90)
        self.tilly.forward(TILE_LENGTH)

    def move_down(self):
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

    def round_int(self, number, base=25):
        return base * round(number / base)
