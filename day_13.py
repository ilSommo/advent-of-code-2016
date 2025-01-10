"""Day 13: A Maze of Twisty Little Cubicles"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque

GOAL = 31 + 39j
START = 1 + 1j


def main():
    """Solve day 13 puzzles."""
    with open("data/day_13.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    number = int(puzzle_input)
    paths = deque()
    paths.append((START, 0))
    best_paths = {START: 0}

    while GOAL not in best_paths:
        path = paths.popleft()
        new_paths, best_paths = perform_step(path, best_paths, number)
        paths.extend(new_paths)

    return best_paths[GOAL]


def star_2(puzzle_input):
    """Solve second puzzle."""
    number = int(puzzle_input)
    paths = deque()
    paths.append((START, 0))
    best_paths = {START: 0}

    while max(best_paths.values()) < 51:
        path = paths.popleft()
        new_paths, best_paths = perform_step(path, best_paths, number)
        paths.extend(new_paths)

    return len(best_paths) - 1


def is_wall(coordinate, number):
    """Check if a given coordinate corresponds to a wall."""
    x = int(coordinate.real)
    y = int(coordinate.imag)

    if bin(x * x + 3 * x + 2 * x * y + y + y * y + number).count("1") % 2 == 0:
        return False

    return True


def perform_step(path, best_paths, number):
    """Perform all possible steps."""
    coordinate, step = path
    step += 1
    new_paths = []

    for direction in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j):
        new_coordinate = coordinate + direction

        if (
            new_coordinate.real >= 0
            and new_coordinate.imag >= 0
            and not is_wall(new_coordinate, number)
            and step < best_paths.get(new_coordinate, float("inf"))
        ):
            new_paths.append((new_coordinate, step))
            best_paths[new_coordinate] = step

    return new_paths, best_paths


if __name__ == "__main__":
    main()
