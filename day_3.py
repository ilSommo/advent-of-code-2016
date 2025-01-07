"""Day 3: Squares With Three Sides"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools


def main():
    """Solve day 3 puzzles."""
    with open("data/day_3.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    triangles = load_triangles(puzzle_input)

    return sum(
        1 for triangle in triangles if triangle[2] < triangle[0] + triangle[1]
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    triangles = load_triangles_vertical(puzzle_input)

    return sum(
        1 for triangle in triangles if triangle[2] < triangle[0] + triangle[1]
    )


def load_triangles(puzzle_input):
    """Load triangles with sorted sides."""
    return tuple(
        tuple(sorted(int(side) for side in line.split()))
        for line in puzzle_input
    )


def load_triangles_vertical(puzzle_input):
    """Load triangles with sorted sides."""
    return tuple(
        tuple(sorted(int(puzzle_input[i + ii].split()[j]) for ii in range(3)))
        for i, j in itertools.product(range(0, len(puzzle_input), 3), range(3))
    )


if __name__ == "__main__":
    main()
