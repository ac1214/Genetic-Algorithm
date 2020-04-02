import sys
from EnvironmentHelpers.Fountain import *
from EnvironmentHelpers.Tilly import *
from EnvironmentHelpers.Tile import *

file_name = ""


def main():
    moves = []
    if(file_name != ""):
        file = open(file_name, "r")
        line = file.readline()

        moves = list(map(int, line.split(", ")))
    print(moves)

    # Generate the fountain
    fountain = Fountain()
    fountain.generate_fountain()

    # Spawn Tilly
    tilly = Tilly(fountain)
    tilly.spawn_tilly()

    turtle.mainloop()


if(len(sys.argv) > 1):
    file_name = sys.argv[1]


main()
