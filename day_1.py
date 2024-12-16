"""Day 1: No Time for a Taxicab"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 1 puzzles."""
    with open("data/day_1.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    instructions = load_instructions(puzzle_input)
    position = 0 + 0j
    direction = 0 + 1j

    for turn, walk in instructions:
        direction *= 1j if turn == "L" else -1j
        position += walk * direction

    return int(abs(position.real) + abs(position.imag))


def star_2(puzzle_input):
    """Solve second puzzle."""
    instructions = load_instructions(puzzle_input)
    position = 0 + 0j
    direction = 0 + 1j

    visited = set()
    found = False

    for turn, walk in instructions:
        direction *= 1j if turn == "L" else -1j

        for _ in range(walk):
            position += direction

            if position in visited:
                found = True
                break

            visited.add(position)

        if found is True:
            break

    return int(abs(position.real) + abs(position.imag))


def load_instructions(puzzle_input):
    """Load instructions from input."""
    return tuple(
        (instruction[0], int(instruction[1:]))
        for instruction in puzzle_input.split(", ")
    )


if __name__ == "__main__":
    main()
