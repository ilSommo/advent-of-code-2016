"""Day 2: Bathroom Security"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

NUMBERS_1 = {
    -1 + 1j: "1",
    0 + 1j: "2",
    1 + 1j: "3",
    -1 + 0j: "4",
    0 + 0j: "5",
    1 + 0j: "6",
    -1 - 1j: "7",
    0 - 1j: "8",
    1 - 1j: "9",
}

NUMBERS_2 = {
    0 + 2j: "1",
    -1 + 1j: "2",
    0 + 1j: "3",
    1 + 1j: "4",
    -2 + 0j: "5",
    -1 + 0j: "6",
    0 + 0j: "7",
    1 + 0j: "8",
    2 + 0j: "9",
    -1 - 1j: "A",
    0 - 1j: "B",
    1 - 1j: "C",
    0 - 2j: "D",
}


def main():
    """Solve day 2 puzzles."""
    with open("data/day_2.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    code = []
    position = 0 + 0j

    for line in puzzle_input:
        for instruction in line:
            position = execute_instruction_1(position, instruction)

        code.append(NUMBERS_1[position])

    return "".join(code)


def star_2(puzzle_input):
    """Solve second puzzle."""
    code = []
    position = -2 + 0j

    for line in puzzle_input:
        for instruction in line:
            position = execute_instruction_2(position, instruction)

        code.append(NUMBERS_2[position])

    return "".join(code)


def execute_instruction(position, instruction):
    """Execute instruction."""
    match instruction:
        case "U":
            position += 1j

        case "D":
            position -= 1j

        case "L":
            position -= 1

        case "R":
            position += 1

    return position


def execute_instruction_1(position, instruction):
    """Execute instruction for first star."""
    new_position = execute_instruction(position, instruction)

    if abs(new_position) < 2:
        position = new_position

    return position


def execute_instruction_2(position, instruction):
    """Execute instruction for second star."""
    new_position = execute_instruction(position, instruction)

    if abs(new_position) <= 2:
        position = new_position

    return position


if __name__ == "__main__":
    main()
