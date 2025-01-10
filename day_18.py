"""Day 18: Like a Rogue"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 18 puzzles."""
    with open("data/day_18.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    rows = [puzzle_input]

    for _ in range(39):
        rows.append(
            "".join(get_tile(rows[-1], i) for i, _ in enumerate(rows[-1]))
        )

    return sum(row.count(".") for row in rows)


def star_2(puzzle_input):
    """Solve second puzzle."""
    rows = [puzzle_input]

    for _ in range(399999):
        rows.append(
            "".join(get_tile(rows[-1], i) for i, _ in enumerate(rows[-1]))
        )

    return sum(row.count(".") for row in rows)


def get_tile(row, position):
    """Get a new tile."""
    tiles = get_tiles(row, position)

    if tiles in ("^^.", ".^^", "^..", "..^"):
        return "^"

    return "."


def get_tiles(row, position):
    """Get relevant tiles for a given position."""
    if position == 0:
        return "." + row[:2]

    if position == len(row) - 1:
        return row[-2:] + "."

    return row[position - 1 : position + 2]


if __name__ == "__main__":
    main()
