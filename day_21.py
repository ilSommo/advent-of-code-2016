"""Day 21: Scrambled Letters and Hash"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 21 puzzles."""
    with open("data/day_21.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    string = "abcdefgh"

    for instruction in puzzle_input:
        string = apply_instruction(instruction, string)

    return string


def star_2(puzzle_input):
    """Solve second puzzle."""
    string = "fbgdceah"

    for instruction in puzzle_input[::-1]:
        string = reverse_instruction(instruction, string)

    return string


def apply_instruction(instruction, string):
    """Apply given instruction on string."""
    chunks = instruction.split()

    if "swap position" in instruction:
        x = min(int(chunks[2]), int(chunks[-1]))
        y = max(int(chunks[2]), int(chunks[-1]))
        string = (
            string[:x]
            + string[y]
            + string[x + 1 : y]
            + string[x]
            + string[y + 1 :]
        )

    elif "swap letter" in instruction:
        x = chunks[2]
        y = chunks[-1]
        string = string.replace(x, ".")
        string = string.replace(y, x)
        string = string.replace(".", y)

    elif "rotate left" in instruction:
        x = int(chunks[2]) % len(string)
        string = string[x:] + string[:x]

    elif "rotate right" in instruction:
        x = int(chunks[2]) % len(string)
        string = string[-x:] + string[:-x]

    elif "rotate" in instruction:
        x = chunks[-1]
        index = (string.index(x) + 1 + int(string.index(x) >= 4)) % len(string)
        string = string[-index:] + string[:-index]

    elif "reverse" in instruction:
        x = min(int(chunks[2]), int(chunks[-1]))
        y = max(int(chunks[2]), int(chunks[-1]))
        string = string[:x] + string[x : y + 1][::-1] + string[y + 1 :]

    elif "move" in instruction:
        x = int(chunks[2])
        y = int(chunks[-1])
        letter = string[x]
        string = string[:x] + string[x + 1 :]
        string = string[:y] + letter + string[y:]

    return string


def reverse_instruction(instruction, string):
    """Reverse given instruction on string."""
    chunks = instruction.split()

    if "rotate left" in instruction:
        x = int(chunks[2]) % len(string)
        string = string[-x:] + string[:-x]

    elif "rotate right" in instruction:
        x = int(chunks[2]) % len(string)
        string = string[x:] + string[:x]

    elif "rotate" in instruction:
        for i in range(len(string)):
            if string == apply_instruction(
                instruction, string[i:] + string[:i]
            ):
                string = string[i:] + string[:i]
                break

    elif "move" in instruction:
        x = int(chunks[-1])
        y = int(chunks[2])
        letter = string[x]
        string = string[:x] + string[x + 1 :]
        string = string[:y] + letter + string[y:]

    else:
        string = apply_instruction(instruction, string)

    return string


if __name__ == "__main__":
    main()
