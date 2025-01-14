"""Day 22: Grid Computing"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools


def main():
    """Solve day 22 puzzles."""
    with open("data/day_22.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    nodes = load_nodes(puzzle_input)
    viable_pairs = {
        (a, b)
        for a, b in itertools.permutations(nodes, 2)
        if nodes[a][1] and nodes[a][1] <= nodes[b][2]
    }

    return len(viable_pairs)


def star_2(puzzle_input):
    """Solve second puzzle."""
    nodes = load_nodes(puzzle_input)
    goal = max(node.real for node in nodes if node.imag == 0) + 0j
    empty = [node for node, sizes in nodes.items() if sizes[1] == 0][0]
    walls = {
        node for node, sizes in nodes.items() if sizes[1] > nodes[empty][0]
    }

    return int(
        2 * (empty.real - min(wall.real for wall in walls) + 1)
        + empty.imag
        + (goal.real - empty.real)
        + 5 * (goal.real - 1)
    )


def load_nodes(puzzle_input):
    """Load nodes from input."""
    nodes = {}

    for line in puzzle_input[2:]:
        chunks = line.split()
        node_chunks = chunks[0].split("-")
        nodes[int(node_chunks[1][1:]) + int(node_chunks[2][1:]) * 1j] = (
            int(chunks[1][:-1]),
            int(chunks[2][:-1]),
            int(chunks[3][:-1]),
        )

    return nodes


if __name__ == "__main__":
    main()
