import os
import string

from base_classes.solution import Solution
from utils import read_data


class Day3Solution(Solution):
    def __init__(self):
        directory = os.path.dirname(__file__)  # current directory
        self.data = read_data(directory, as_2d_array=True)

    def part1(self):
        """
        Calculate the sum of numbers adjacent to valid symbols in the data.

        Returns:
            int: The sum of adjacent numbers.
        """
        num_sum = 0
        for i, row in enumerate(self.data):
            number = ""
            for j, char in enumerate(row):
                if char.isdigit():
                    number += char
                    if j + 1 < len(row):
                        char = row[j + 1]
                elif number and self.check_adjacent_symbols(i, j, len(number)):
                    num_sum += int(number)
                    number = ""
                else:
                    number = ""
        return num_sum

    def check_adjacent_symbols(self, i, j, length):
        """
        Check if there are any valid symbols adjacent to the given coordinates.

        Args:
            i (int): The row index.
            j (int): The column index.
            length (int): The length of the number.

        Returns:
            bool: True if there are any valid symbols adjacent to the given coordinates, False otherwise.
        """
        directions = [
            # cardinals
            (-1, 0),  # left
            (1, 0),  # right
            (0, -1),  # up
            (0, 1),  # down
            # diagonals
            (-1, -1),  # left-up
            (-1, 1),  # left-down
            (1, -1),  # right-up
            (1, 1),  # right-down
        ]
        # go through each direction
        for dx, dy in directions:
            # do this for each character in the number
            for k in range(length):
                # get the coordinates of the character
                x, y = i + dx, j - k + dy
                if (
                    # check if it is within the bounds of the data
                    0 <= x < len(self.data)
                    and 0 <= y < len(self.data[0])
                    # check if it is a valid symbol
                    and self.is_valid_symbol(self.data[x][y])
                ):
                    return True
        return False

    def is_valid_symbol(self, char):
        """
        Check if the given character is a valid symbol.

        Args:
            char (str): The character to check.

        Returns:
            bool: True if the character is a valid symbol, False otherwise.
        """
        return char not in string.ascii_letters + string.digits and char != "."

    def part2(self):
        """
        Solve part 2 of the problem.

        Returns:
            Any: The solution for part 2.
        """
        pass
