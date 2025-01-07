"""Day 4: Security Through Obscurity"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import Counter


def main():
    """Solve day 4 puzzles."""
    with open("data/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    rooms = load_rooms(puzzle_input)

    return sum(
        room[1] for room in rooms if compute_checksum(room[0]) == room[2]
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    rooms = load_rooms(puzzle_input)

    for name, sector, _ in rooms:
        if decrypt_name(name, sector) == "northpole object storage":
            return sector

    return -1


def compute_checksum(name):
    """Compute checksum of a room name."""
    counter = Counter(sorted(name.replace("-", "")))

    return "".join(element[0] for element in counter.most_common(5))


def decrypt_name(name, sector):
    """Decrypt room name."""
    name = name.replace("-", " ")
    decrypted_name = []

    for letter in name:
        if letter != " ":
            letter = chr(((ord(letter) - 97) + sector) % 26 + 97)

        decrypted_name.append(letter)

    return "".join(decrypted_name)


def load_rooms(puzzle_input):
    """Load rooms from input."""
    rooms = []

    for line in puzzle_input:
        string, checksum = line[:-1].split("[")
        letters = "-".join(string.split("-")[:-1])
        sector = int(string.split("-")[-1])
        rooms.append((letters, sector, checksum))

    return tuple(rooms)


if __name__ == "__main__":
    main()
