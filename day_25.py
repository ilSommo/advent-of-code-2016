"""Day 25: Clock Signal"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 25 puzzles."""
    with open("data/day_25.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    a = 0

    while True:
        registers = {k: 0 for k in ("b", "c", "d")}
        registers["a"] = a

        output = []
        instructions = [[]]
        i = 0

        while i < len(puzzle_input):
            instructions[-1].append(puzzle_input[i])
            registers, i, new_output = execute_instruction(
                registers, puzzle_input, i, output
            )

            if new_output != output:
                if new_output[-1] != len(output) % 2:
                    break

                for j in range(len(instructions) // 2):
                    if (
                        len(instructions) >= j
                        and instructions[-j:] == instructions[-2 * j : -j]
                    ):
                        return a

                if new_output[-1] == 1:
                    instructions.append([])

            output = new_output

        a += 1


def execute_instruction(registers, instructions, i, output):
    """Execute the given instruction."""
    instruction = instructions[i].split()
    new_output = output.copy()

    match instruction[0]:
        case "cpy":
            if instruction[2].islower():
                registers[instruction[2]] = get_value(
                    instruction[1], registers
                )

        case "inc":
            registers[instruction[1]] += 1

        case "dec":
            registers[instruction[1]] -= 1

        case "jnz":
            if get_value(instruction[1], registers) != 0:
                i += get_value(instruction[2], registers) - 1

        case "out":
            new_output.append(get_value(instruction[1], registers))

    i += 1

    return registers, i, new_output


def get_value(x, registers):
    """Return literl value or value of register."""
    return registers[x] if x.islower() else int(x)


if __name__ == "__main__":
    main()
