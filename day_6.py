"""Day 6: Signals and Noise"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools
from collections import Counter


def main():
    """Solve day 6 puzzles."""
    with open("data/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    counters = load_counters(puzzle_input)

    return "".join(counter.most_common()[0][0] for counter in counters)


def star_2(puzzle_input):
    """Solve second puzzle."""
    counters = load_counters(puzzle_input)

    return "".join(counter.most_common()[-1][0] for counter in counters)


def load_counters(puzzle_input):
    """Load counters from input."""
    counters = [Counter() for _ in range(len(puzzle_input[0]))]

    for line, i in itertools.product(
        puzzle_input, range(len(puzzle_input[0]))
    ):
        counters[i].update(line[i])

    return tuple(counters)


if __name__ == "__main__":
    main()
