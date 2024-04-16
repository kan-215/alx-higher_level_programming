def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read(), end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Example usage:
read_file("my_file_0.txt")
