#!/usr/bin/env python3
import math
from typing import Tuple


def get_player_pos() -> Tuple[float, float, float]:
    while True:
        try:
            user_input = input("Enter new coordinates "
                               "as floats in format 'x,y,z': ")
            input_list: list[str] = []
            input_list = user_input.split(",")
            x = float(input_list[0].strip())
            y = float(input_list[1].strip())
            z = float(input_list[2].strip())

            return (x, y, z)
        except ValueError:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    first_set = get_player_pos()
    distance1 = math.sqrt((first_set[0]-0)**2 +
                          (first_set[1]-0)**2 +
                          (first_set[2]-0)**2)

    print(f"Got the first tuple: "
          f"({first_set[0]}, "
          f"{first_set[1]}, "
          f"{first_set[2]})"
          )
    print(f"It includes: "
          f"X={first_set[0]}, "
          f"Y={first_set[1]}, "
          f"Z={first_set[2]}"
          )

    print(f"Distance to center: {round(distance1, 4)}")
    print("\nGet a second set of coordinates")

    second_set = get_player_pos()

    distance2 = math.sqrt((second_set[0]-first_set[0])**2 +
                          (second_set[1]-first_set[1])**2 +
                          (second_set[2]-first_set[2])**2)
    print(f"distance to center: {round(distance2, 4)}")


main()
