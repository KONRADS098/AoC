import os
from base_classes.solution import Solution
from utils import read_data


class Day1Solution(Solution):
    def __init__(self):
        directory = os.path.dirname(__file__)  # current directory
        self.data = read_data(directory)

    def part1(self):
        sum = 0

        for i in self.data:
            cal_val = ""

            # left side
            for j in range(len(i)):
                if i[j].isdigit():
                    cal_val += i[j]
                    break

            # right side
            for j in range(len(i) - 1, -1, -1):
                if i[j].isdigit():
                    cal_val += i[j]
                    break

            # here we combine the string value
            sum += int(cal_val)

        return sum

    def part2(self):
        pass
