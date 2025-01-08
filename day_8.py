"""Day 8: Two-Factor Authentication"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools

N_COLUMNS = 50
N_ROWS = 6


def main():
    """Solve day 8 puzzles."""
    with open("data/day_8.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    operations = load_operations(puzzle_input)
    pixels = perform_operations(operations)

    return len(pixels)


def star_2(puzzle_input):
    """Solve second puzzle."""
    operations = load_operations(puzzle_input)
    pixels = perform_operations(operations)

    return "\n".join(
        "".join("#" if i + j * 1j in pixels else " " for j in range(N_COLUMNS))
        for i in range(N_ROWS)
    )


def load_operations(puzzle_input):
    """Load operations from input."""
    operations = []

    for line in puzzle_input:
        chunks = line.split()

        if chunks[0] == "rect":
            i, j = chunks[1].split("x")
            operations.append(("rect", int(i), int(j)))

        elif chunks[1] == "row":
            row = int(chunks[2].split("=")[-1])
            operations.append(("row", row, int(chunks[-1]) * 1j))

        elif chunks[1] == "column":
            column = int(chunks[2].split("=")[-1])
            operations.append(("column", column, int(chunks[-1])))

    return tuple(operations)


def perform_operations(operations):
    """Perform operations."""
    pixels = []

    for operation in operations:
        match operation[0]:
            case "rect":
                for i, j in itertools.product(
                    range(operation[2]), range(operation[1])
                ):
                    pixels.append(i + j * 1j)

            case "row":
                for i, pixel in enumerate(pixels):
                    if pixel.real == operation[1]:
                        pixels[i] = pixel + operation[2]

            case "column":
                for i, pixel in enumerate(pixels):
                    if pixel.imag == operation[1]:
                        pixels[i] = pixel + operation[2]

        for i, pixel in enumerate(pixels):
            pixels[i] = pixel.real % N_ROWS + pixel.imag % N_COLUMNS * 1j

        pixels = list(set(pixels))

    return tuple(pixels)


if __name__ == "__main__":
    main()
