"""Day 9: Explosives in Cyberspace"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 9 puzzles."""
    with open("data/day_9.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    decompressed = decompress(puzzle_input)

    return sum(len(chunk[0]) * chunk[1] for chunk in decompressed)


def star_2(puzzle_input):
    """Solve second puzzle."""
    decompressed = deque(decompress(puzzle_input))
    total = 0

    while decompressed:
        chunk = decompressed.popleft()

        if "(" not in chunk[0]:
            total += len(chunk[0]) * chunk[1]

        else:
            decompressed.extend(decompress(chunk[0], chunk[1]))

    return total


def decompress(text, multiplier=1):
    """Decompress a text."""
    decompressed = []
    i = 0

    while i < len(text):
        if text[i] != "(":
            decompressed.append((text[i], multiplier))

        else:
            x = text[i:].find("x") + i
            end = text[i:].find(")") + i
            characters = int(text[i + 1 : x])
            times = int(text[x + 1 : end])
            decompressed.append(
                (text[end + 1 : end + characters + 1], times * multiplier)
            )

            i = end + characters

        i += 1

    return decompressed


if __name__ == "__main__":
    main()
