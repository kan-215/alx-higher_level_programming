def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Example usage:
characters_written = write_file("my_first_file.txt", text)
print(characters_written)

# Read and print the contents of the file
try:
    with open("my_first_file.txt", 'r', encoding='utf-8') as file:
        print(file.read(), end='')
except FileNotFoundError:
    print("Error: File not found.")
