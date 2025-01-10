"""Day 16: Dragon Checksum"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

LENGTH_1 = 272
LENGTH_2 = 35651584


def main():
    """Solve day 16 puzzles."""
    with open("data/day_16.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    string = puzzle_input

    while len(string) < LENGTH_1:
        string = perform_step(string)

    return checksum(string[:LENGTH_1])


def star_2(puzzle_input):
    """Solve second puzzle."""
    string = puzzle_input

    while len(string) < LENGTH_2:
        string = perform_step(string)

    return checksum(string[:LENGTH_2])


def checksum(string):
    """Generate the checksum of a string."""
    while len(string) % 2 == 0:
        string = "".join(
            "1" if string[i] == string[i + 1] else "0"
            for i in range(0, len(string), 2)
        )

    return string


def perform_step(a):
    """Perform a single step."""
    b = a[::-1]

    b = b.replace("0", ".")
    b = b.replace("1", "0")
    b = b.replace(".", "1")

    return a + "0" + b


if __name__ == "__main__":
    main()
