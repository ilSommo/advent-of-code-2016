"""Day 23: Safe Cracking"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 23 puzzles."""
    with open("data/day_23.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    instructions = list(puzzle_input)
    registers = {k: 0 for k in ("b", "c", "d")}
    registers["a"] = 7
    i = 0

    while i < len(instructions):
        registers, instructions, i = execute_instruction(
            registers, instructions, i
        )

    return registers["a"]


def star_2(puzzle_input):
    """Solve second puzzle."""
    instructions = list(puzzle_input)
    registers = {k: 0 for k in ("b", "c", "d")}
    registers["a"] = 12
    i = 0

    while i < len(instructions):
        registers, instructions, i = execute_instruction(
            registers, instructions, i
        )

    return registers["a"]


def execute_instruction(registers, instructions, i):
    """Execute the given instruction."""
    if is_mul(instructions, i):
        registers[instructions[i + 1].split()[1]] += get_value(
            instructions[i].split()[1], registers
        ) * get_value(instructions[i + 4].split()[1], registers)
        registers[instructions[i + 2].split()[1]] = 0
        registers[instructions[i + 4].split()[1]] = 0
        i += 6

        return registers, instructions, i

    instruction = instructions[i].split()

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

        case "tgl":
            x = i + get_value(instruction[1], registers)

            if 0 <= x < len(instructions):

                if "inc" in instructions[x]:
                    instructions[x] = instructions[x].replace("inc", "dec")

                elif "dec" in instructions[x]:
                    instructions[x] = instructions[x].replace("dec", "inc")

                elif "tgl" in instructions[x]:
                    instructions[x] = instructions[x].replace("tgl", "inc")

                elif "jnz" in instructions[x]:
                    instructions[x] = instructions[x].replace("jnz", "cpy")

                elif "cpy" in instructions[x]:
                    instructions[x] = instructions[x].replace("cpy", "jnz")

    i += 1

    return registers, instructions, i


def get_value(x, registers):
    """Return literl value or value of register."""
    return registers[x] if x.islower() else int(x)


def is_mul(instructions, i):
    """Check if an instruction loop is a multiplication."""
    if not "cpy" in instructions[i]:
        return False

    if not ("inc" in instructions[i + 1] and "dec" in instructions[i + 2]):
        return False

    if not ("jnz" in instructions[i + 3] and "-2" in instructions[i + 3]):
        return False

    if not "dec" in instructions[i + 4]:
        return False

    if not ("jnz" in instructions[i + 5] and "-5" in instructions[i + 5]):
        return False

    return True


if __name__ == "__main__":
    main()
