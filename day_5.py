"""Day 5: How About a Nice Game of Chess?"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import hashlib


def main():
    """Solve day 5 puzzles."""
    with open("data/day_5.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    password = []
    index = 0

    while len(password) < 8:
        if (
            hashlib.md5(f"{puzzle_input}{index}".encode())
            .hexdigest()
            .startswith(5 * "0")
        ):
            password.append(
                hashlib.md5(f"{puzzle_input}{index}".encode()).hexdigest()[5]
            )

        index += 1

    return "".join(password)


def star_2(puzzle_input):
    """Solve second puzzle."""
    password = {}
    index = 0

    while len(password) < 8:
        if (
            hashlib.md5(f"{puzzle_input}{index}".encode())
            .hexdigest()
            .startswith(5 * "0")
        ):
            hash_result = hashlib.md5(
                f"{puzzle_input}{index}".encode()
            ).hexdigest()

            if (
                hash_result[5].isdigit()
                and int(hash_result[5]) < 8
                and int(hash_result[5]) not in password
            ):
                password[int(hash_result[5])] = hash_result[6]

        index += 1

    return "".join(v for _, v in sorted(password.items()))


if __name__ == "__main__":
    main()
