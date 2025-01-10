"""Day 20: Firewall Rules"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 20 puzzles."""
    with open("data/day_20.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    ranges = sorted(load_ranges(puzzle_input), key=lambda range_: range_[1])

    for range_0 in ranges:
        candidate = range_0[-1] + 1
        flag = True

        for range_1 in ranges:
            if candidate in range_1:
                flag = False
                break

        if flag:
            return candidate

    return None


def star_2(puzzle_input):
    """Solve second puzzle."""
    ranges = load_ranges(puzzle_input)
    forbidden_ranges = []

    for range_0 in ranges:
        a = range_0[0]
        b = range_0[-1]
        bad_ranges = set()

        for range_1 in forbidden_ranges:
            if a in range_1:
                bad_ranges.add(range_1)
                a = range_1[0]

            if b in range_1:
                bad_ranges.add(range_1)
                b = range_1[-1]

            if range_1[0] in range_0 and range_1[-1] in range_0:
                bad_ranges.add(range_1)

        for bad_range in bad_ranges:
            forbidden_ranges.remove(bad_range)

        forbidden_ranges.append(range(a, b + 1))

    return 4294967296 - sum(len(range_) for range_ in forbidden_ranges)


def load_ranges(puzzle_input):
    """Load ranges from input."""
    return tuple(
        range(int(line.split("-")[0]), int(line.split("-")[1]) + 1)
        for line in puzzle_input
    )


if __name__ == "__main__":
    main()
