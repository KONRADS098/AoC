import os


def read_data(directory, file_name="input.txt"):
    """
    Reads the data from the input.txt file and returns it as a list of strings

    Returns:
        list: A list of strings
    """
    with open(os.path.join(directory, file_name), "r") as f:
        print(f"Reading data from {os.path.join(directory, file_name)}")
        print("===============================================")
        return f.read().splitlines()
