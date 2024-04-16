#!/usr/bin/python3

def read_file(filename=""):
    """
    Read the contents of a text file and print it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())


if __name__ == "__main__":
    read_file("my_file_0.txt")
