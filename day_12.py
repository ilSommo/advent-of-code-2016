"""Day 12: Leonardo's Monorail"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 12 puzzles."""
    with open("data/day_12.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    registers = {k: 0 for k in ("a", "b", "c", "d")}
    i = 0

    while i < len(puzzle_input):
        registers, i = execute_instruction(registers, puzzle_input, i)

    return registers["a"]


def star_2(puzzle_input):
    """Solve second puzzle."""
    registers = {k: 0 for k in ("a", "b", "d")}
    registers["c"] = 1
    i = 0

    while i < len(puzzle_input):
        registers, i = execute_instruction(registers, puzzle_input, i)

    return registers["a"]


def execute_instruction(registers, instructions, i):
    """Execute the given instruction."""
    instruction = instructions[i].split()

    match instruction[0]:
        case "cpy":
            registers[instruction[2]] = (
                int(instruction[1])
                if instruction[1].isdigit()
                else registers[instruction[1]]
            )

        case "inc":
            registers[instruction[1]] += 1

        case "dec":
            registers[instruction[1]] -= 1

        case "jnz":
            if registers.get(instruction[1], 0) or (
                instruction[1].isdigit() and instruction[1] != 0
            ):
                i += int(instruction[2]) - 1

    i += 1

    return registers, i


if __name__ == "__main__":
    main()
