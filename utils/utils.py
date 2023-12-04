import os


def read_data(directory, file_name="input.txt", as_2d_array=False):
    """
    Reads the data from the input.txt file and returns it as a list of strings or a 2D array

    Args:
        directory (str): The directory where the file is located
        file_name (str): The name of the file to read (default: "input.txt")
        as_2d_array (bool): Whether to return the data as a 2D array (default: False)

    Returns:
        list or list of lists: A list of strings or a 2D array
    """
    with open(os.path.join(directory, file_name), "r") as f:
        print(f"Reading data from {os.path.join(directory, file_name)}")
        print("===============================================")
        if as_2d_array:
            return [list(line) for line in f.read().splitlines()]
        else:
            return f.read().splitlines()
