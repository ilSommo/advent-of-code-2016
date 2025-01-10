"""Day 17: Two Steps Forward"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import hashlib
from collections import deque

DIRECTION_TO_INDEX = {0 + 1j: 0, 0 - 1j: 1, -1 + 0j: 2, 1 + 0j: 3}
DIRECTION_TO_LETTER = {0 + 1j: "U", 0 - 1j: "D", -1 + 0j: "L", 1 + 0j: "R"}
GOAL = 3 + 0j
OPEN = ("b", "c", "d", "e", "f")
START = 0 + 3j


def main():
    """Solve day 17 puzzles."""
    with open("data/day_17.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    paths = deque()
    paths.append((START, ""))

    while paths:
        path = paths.popleft()

        if path[0] == GOAL:
            return path[1]

        paths.extend(perform_step(path, puzzle_input))

    return None


def star_2(puzzle_input):
    """Solve second puzzle."""
    paths = deque()
    paths.append((START, ""))
    complete_paths = []

    while paths:
        path = paths.popleft()

        if path[0] == GOAL:
            complete_paths.append(path[1])
            continue

        paths.extend(perform_step(path, puzzle_input))

    return len(max(complete_paths, key=len))


def perform_step(path, passcode):
    """Perform a single step."""
    new_paths = []
    position, steps = path
    hash_directions = hashlib.md5(f"{passcode}{steps}".encode()).hexdigest()[
        :4
    ]

    for direction, index in DIRECTION_TO_INDEX.items():
        new_position = position + direction

        if (
            0 <= new_position.real < 4
            and 0 <= new_position.imag < 4
            and hash_directions[index] in OPEN
        ):
            new_paths.append(
                (new_position, steps + DIRECTION_TO_LETTER[direction])
            )

    return new_paths


if __name__ == "__main__":
    main()
