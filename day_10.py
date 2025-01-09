"""Day 10: Balance Bots"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

from collections import defaultdict, deque


def main():
    """Solve day 10 puzzles."""
    with open("data/day_10.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    instructions = load_instructions(puzzle_input)

    _, target_bot = execute_instructions(instructions)

    return target_bot


def star_2(puzzle_input):
    """Solve second puzzle."""
    instructions = load_instructions(puzzle_input)

    output, _ = execute_instructions(instructions)

    return output[0] * output[1] * output[2]


def execute_instructions(instructions):
    """Execute the instructions."""
    bots = defaultdict(set)
    output = {}
    target_bot = -1

    while instructions:
        instruction = instructions.popleft()

        if instruction[0] == "value":
            bots[instruction[2]].add(instruction[1])

        elif len(bots[instruction[0]]) == 2:
            values = bots.pop(instruction[0])

            if min(values) == 17 and max(values) == 61:
                target_bot = instruction[0]

            if instruction[1] == "bot":
                bots[instruction[2]].add(min(values))

            else:
                output[instruction[2]] = min(values)

            if instruction[3] == "bot":
                bots[instruction[4]].add(max(values))

            else:
                output[instruction[4]] = max(values)

        else:
            instructions.append(instruction)

    return output, target_bot


def load_instructions(puzzle_input):
    """Load instructions from input."""
    instructions = deque()

    for line in puzzle_input:
        chunks = line.split()

        if chunks[0] == "value":
            instructions.append(("value", int(chunks[1]), int(chunks[-1])))

        else:
            instructions.append(
                (
                    int(chunks[1]),
                    chunks[5],
                    int(chunks[6]),
                    chunks[-2],
                    int(chunks[-1]),
                )
            )

    return instructions


if __name__ == "__main__":
    main()
