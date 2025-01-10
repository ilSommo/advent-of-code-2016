"""Day 14: One-Time Pad"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import hashlib
import re
from functools import cache


def main():
    """Solve day 14 puzzles."""
    with open("data/day_14.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    keys = 0
    i = -1

    while keys < 64:
        i += 1

        triplet = re.search(
            r"(.)\1\1", hashlib.md5(f"{puzzle_input}{i}".encode()).hexdigest()
        )

        if triplet:
            for j in range(1000):
                if (
                    5 * triplet.group()[0]
                    in hashlib.md5(
                        f"{puzzle_input}{i+j+1}".encode()
                    ).hexdigest()
                ):
                    keys += 1
                    break

    return i


def star_2(puzzle_input):
    """Solve second puzzle."""
    keys = 0
    i = -1

    while keys < 64:
        i += 1

        triplet = re.search(r"(.)\1\1", hash_stretch(f"{puzzle_input}{i}"))

        if triplet:
            for j in range(1000):
                if 5 * triplet.group()[0] in hash_stretch(
                    f"{puzzle_input}{i+j+1}"
                ):
                    keys += 1
                    break

    return i


@cache
def hash_stretch(string):
    """Compute the hash stretch of a string."""
    for _ in range(2017):
        string = hashlib.md5(string.encode()).hexdigest()

    return string


if __name__ == "__main__":
    main()
