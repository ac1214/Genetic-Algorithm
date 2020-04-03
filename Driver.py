import sys
from EnvironmentHelpers.Fountain import *
from EnvironmentHelpers.Tilly import *
from EnvironmentHelpers.Tile import *
import time

file_name = ""
max_moves = 200


def main():
    moves = []
    if(file_name != ""):
        file = open(file_name, "r")
        line = file.readline()

        moves = list(map(int, line.split(" ")))
    print("Loaded Tilly: ", moves)

    # Generate the fountain
    fountain = Fountain()
    fountain.generate_fountain()

    # Spawn Tilly
    tilly = Tilly(fountain, moves)
    tilly.spawn_tilly()

    for i in range(1, max_moves + 1):
        tilly.make_move()
        tilly.fountain.clear_board()
        tilly.update_earnings()
        tilly.update_energy(i)

    turtle.mainloop()


if(len(sys.argv) > 1):
    file_name = sys.argv[1]
else:
    print("Add a Tilly moveset file as the first argument")
    exit(1)


main()
