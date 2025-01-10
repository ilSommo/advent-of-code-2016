"""Day 19: An Elephant Named Joseph"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 19 puzzles."""
    with open("data/day_19.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    elves = deque(k + 1 for k in range(int(puzzle_input)))

    while len(elves) != 1:
        elves.rotate(-1)
        elves.popleft()

    return elves[0]


def star_2(puzzle_input):
    """Solve second puzzle."""
    elves_0 = deque(k + 1 for k in range(int(puzzle_input) // 2))
    elves_1 = deque(
        k + 1 for k in range(int(puzzle_input) // 2, int(puzzle_input))
    )

    while len(elves_0) + len(elves_1) != 1:
        elf_0 = elves_0.popleft()

        if len(elves_0) == len(elves_1):
            elves_0.pop()

        else:
            elves_1.popleft()

        elves_1.append(elf_0)
        elves_0.append(elves_1.popleft())

    return (elves_0 + elves_1)[0]


if __name__ == "__main__":
    main()
