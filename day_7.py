"""Day 7: Internet Protocol Version 7"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import itertools
import re


def main():
    """Solve day 7 puzzles."""
    with open("data/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return sum(
        1
        for line in puzzle_input
        if not re.search(r"\[[^]]*(.)(?!\1)(.)\2\1[^]]*\]", line)
        and re.search(r"(.)(?!\1)(.)\2\1", line)
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    total = 0

    for line in puzzle_input:
        outside, inside = split_line(line)
        patterns = get_patterns(outside)

        for pattern, chunk in itertools.product(patterns, inside):
            reverse_pattern = pattern[1] + pattern[0] + pattern[1]

            if reverse_pattern in chunk:
                total += 1
                break

    return total


def get_patterns(chunks):
    """Get ABA patterns from chunks."""
    patterns = set()

    for chunk in chunks:
        patterns.update(
            match[0] for match in re.findall(r"(?=((.)(?!\2).\2))", chunk)
        )

    return patterns


def split_line(line):
    """Split line in chunks inside and outside of brackets."""
    chunks = line.split("[")
    outside = [chunks[0]]
    inside = []

    for chunk in chunks[1:]:
        outside.append(chunk.split("]")[1])
        inside.append(chunk.split("]")[0])

    return outside, inside


if __name__ == "__main__":
    main()
