import os
import string

from base_classes.solution import Solution
from utils import read_data


class Day4Solution(Solution):
    def __init__(self):
        directory = os.path.dirname(__file__)  # current directory
        self.data = read_data(directory)

    def part1(self):
        total = 0

        for card in self.data:
            nums = card.split(" ")
            nums = [num for num in nums if num.isdigit() or num == "|"]
            split = nums.index("|")
            win = nums[:split]
            pred = nums[split + 1 :]

            points = 0

            for i in win:
                if i in pred:
                    if points == 0:
                        points += 1
                    else:
                        points *= 2
            total += points

        return total
    def part2(self):
        pass
