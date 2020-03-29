from Helpers.Fountain import *


class Tilly:
    def __init__(self):
        self.tilly = turtle.Turtle()
        self.tilly.shape(TILLY)

    def move_tilly(self):
        self.tilly.forward(200)