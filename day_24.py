"""Day 24: Air Duct Spelunking"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools
from collections import deque
from functools import cache


def main():
    """Solve day 24 puzzles."""
    with open("data/day_24.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    points, walls = load_map(puzzle_input)
    distances = compute_distances(points, walls)

    del points[0]

    total_distances = []

    for order in itertools.permutations(points):
        order = (0,) + order
        total_distances.append(
            sum(
                distances[(order[i], order[i + 1])]
                for i in range(len(order) - 1)
            )
        )

    return min(total_distances)


def star_2(puzzle_input):
    """Solve second puzzle."""
    points, walls = load_map(puzzle_input)
    distances = compute_distances(points, walls)

    del points[0]

    total_distances = []

    for order in itertools.permutations(points):
        order = (0,) + order + (0,)
        total_distances.append(
            sum(
                distances[(order[i], order[i + 1])]
                for i in range(len(order) - 1)
            )
        )

    return min(total_distances)


@cache
def compute_distance(start, end, walls):
    """Compute distance between two points."""
    paths = deque([(start, 0)])
    best_paths = {}

    while end not in best_paths:
        position, step = paths.popleft()
        step += 1

        for direction in (1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j):
            new_position = position + direction

            if new_position not in walls and step < best_paths.get(
                new_position, float("inf")
            ):
                paths.append((new_position, step))
                best_paths[new_position] = step

    return best_paths[end]


def compute_distances(points, walls):
    """Compute distances between all point pairs."""
    distances = {}

    for point_0, point_1 in itertools.combinations(points.items(), 2):
        distances[(point_0[0], point_1[0])] = compute_distance(
            point_0[1], point_1[1], walls
        )
        distances[(point_1[0], point_0[0])] = distances[
            (point_0[0], point_1[0])
        ]

    return distances


def load_map(puzzle_input):
    """Load map from input."""
    points = {}
    walls = []

    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char == "#":
                walls.append(i + j * 1j)

            elif char.isdigit():
                points[int(char)] = i + j * 1j

    return dict(sorted(points.items())), tuple(walls)


if __name__ == "__main__":
    main()
