from Helpers.Fountain import *


class Tilly:
    def __init__(self):
        self.tilly = turtle.Turtle()
        self.tilly.penup()
        self.tilly.shape(TILLY)
        turtle.listen()

    def spawn_tilly(self):
        self.tilly.setpos((-225, 225))

    def move_up(self):
        self.tilly.setheading(90)
        self.tilly.forward(50)

    def move_down(self):
        self.tilly.setheading(270)
        self.tilly.forward(50)

    def move_left(self):
        self.tilly.setheading(180)
        self.tilly.forward(50)

    def move_right(self):
        self.tilly.setheading(0)
        self.tilly.forward(50)
