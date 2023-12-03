import os
from base_classes.solution import Solution
from utils import read_data


class Day2Solution(Solution):
    def __init__(self):
        directory = os.path.dirname(__file__)  # current directory
        self.data = read_data(directory)

    def part1(self):
        CONF_RED = 12
        CONF_GREEN = 13
        CONF_BLUE = 14

        id_sum = 0

        for game in self.data:
            id = int(game.split(":")[0].replace("Game ", ""))
            sets = game.split(":")[1].split(";")

            valid_game = True

            for set in sets:
                set = set.lstrip()
                cubes = set.split(",")

                for cube in cubes:
                    cube = cube.lstrip()
                    count = int(cube.split(" ")[0])
                    color = cube.split(" ")[1]

                    if (
                        (color == "red" and count > CONF_RED)
                        or (color == "green" and count > CONF_GREEN)
                        or (color == "blue" and count > CONF_BLUE)
                    ):
                        valid_game = False
                        break

                # Break outer loop if any cube is above threshold
                if not valid_game:
                    break

            # If no cube is above threshold, add id to sum
            if valid_game:
                id_sum += id

        return id_sum

    def part2(self):
        pass
