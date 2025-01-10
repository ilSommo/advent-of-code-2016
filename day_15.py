"""Day 15: Timing is Everything"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 15 puzzles."""
    with open("data/day_15.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    discs = load_discs(puzzle_input)

    return compute_first_time(discs)


def star_2(puzzle_input):
    """Solve second puzzle."""
    discs = load_discs(puzzle_input)
    discs.append([11, 0])

    return compute_first_time(discs)


def compute_first_time(discs):
    """Compute first time discs are in sync."""
    for i, disc in enumerate(discs):
        discs[i] = [disc[0], (disc[1] + i + 1) % disc[0]]

    time = 0

    while sum(disc[1] for disc in discs):
        time += 1

        for i, disc in enumerate(discs):
            discs[i] = [disc[0], (disc[1] + 1) % disc[0]]

    return time


def load_discs(puzzle_input):
    """Load discs from input."""
    discs = []

    for line in puzzle_input:
        chunks = line.rstrip(".").split()
        discs.append([int(chunks[3]), int(chunks[-1])])

    return discs


if __name__ == "__main__":
    main()
