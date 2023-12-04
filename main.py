import os


def main():
    # get the parent directory of the current file
    aoc_folder = os.path.dirname(os.path.abspath(__file__))
    
    for folder_name in reversed(os.listdir(aoc_folder)):
        folder_path = os.path.join(aoc_folder, folder_name)
        print(f"Checking {folder_path}")
        if os.path.isdir(folder_path):
            module_name = f"aoc2023.{folder_name}.{folder_name}"
            print(f"Importing {module_name}")
            module = __import__(module_name, fromlist=[folder_name])
            print(f"Imported {module_name}")
            solution_class = getattr(module, f"{folder_name.capitalize()}Solution")
            print(f"Running {folder_name.capitalize()}")
            solution = solution_class()
            part_1 = solution.part1()
            print(f"{folder_name.capitalize()} - Part 1: {part_1}")
            part_2 = solution.part2()
            print(f"{folder_name.capitalize()} - Part 2: {part_2}")
            print("===============================================")


if __name__ == "__main__":
    main()
