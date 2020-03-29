from EnvironmentHelpers.Fountain import *
from EnvironmentHelpers.Tilly import *
from EnvironmentHelpers.Tile import *


def main():
    # Generate the fountain
    fountain = Fountain()
    fountain.generate_fountain()

    # Spawn Tilly
    tilly = Tilly(fountain)
    tilly.spawn_tilly()

    turtle.mainloop()

main()