from Helpers.Fountain import *
from Helpers.Tilly import *
from Helpers.Tile import *


def main():
    # Generate the fountain
    fountain = Fountain()
    fountain.generate_fountain()

    # Spawn Tilly
    tilly = Tilly()
    tilly.spawn_tilly()

    # Listen for any movements
    turtle.listen()
    turtle.onkey(tilly.move_up, 'Up')
    turtle.onkey(tilly.move_down, 'Down')
    turtle.onkey(tilly.move_left, 'Left')
    turtle.onkey(tilly.move_right, 'Right')
    turtle.mainloop()

main()