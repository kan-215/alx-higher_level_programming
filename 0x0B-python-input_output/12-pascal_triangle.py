#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print Pascal's triangle.

    Args:
        triangle (list of lists): Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
