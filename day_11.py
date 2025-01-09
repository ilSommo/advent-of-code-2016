"""Day 11: Radioisotope Thermoelectric Generators"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2025"
__license__ = "MIT"

import copy
import itertools
from collections import deque
from functools import cache


def main():
    """Solve day 11 puzzles."""
    with open("data/day_11.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    floors = load_floors(puzzle_input)

    return compute_step_number(floors)


def star_2(puzzle_input):
    """Solve second puzzle."""
    floors = load_floors(puzzle_input)
    floors[0].update(
        {"elerium", "elerium-compatible", "dilithium", "dilithium-compatible"}
    )

    return compute_step_number(floors)


@cache
def check_safety(floor):
    """Check safety of floor."""
    generators = set()
    microchips = set()

    for object_ in floor:
        if "compatible" in object_:
            microchips.add(object_)

        else:
            generators.add(object_)

    for microchip in microchips:
        if generators and microchip.split("-")[0] not in generators:
            return False

    return True


def compute_step_number(floors):
    """Compute the number of steps to solve the puzzle."""
    total = sum(len(floor) for floor in floors)
    best_paths = {floors_to_tuple(floors): 0}
    paths = deque()
    paths.append((floors, 0))

    while len(paths[0][0][-1]) < total:
        paths, best_paths = perform_step(paths, best_paths)

    return paths[0][1]


def floor_to_hashable(floor):
    """Make floor hashable."""
    hashable_floor = set()
    generators = set()
    microchips = set()

    for object_ in floor:
        if "elevator" in object_:
            hashable_floor.add("elevator")

        elif "compatible" in object_:
            microchips.add(object_)

        else:
            generators.add(object_)

    i = 0

    for i, generator in enumerate(generators):
        hashable_floor.add(f"generator-{i}")

        if f"{generator}-compatible" in microchips:
            microchips.remove(f"{generator}-compatible")
            hashable_floor.add(f"microchip-{i}")

    hashable_floor.update(
        {f"microchip-{j+i+1}" for j, microchip in enumerate(microchips)}
    )

    return frozenset(hashable_floor)


def floors_to_tuple(floors):
    """Make floors hashable."""
    return tuple(floor_to_hashable(floor) for floor in floors)


def load_floors(puzzle_input):
    """Load floors content from input."""
    floors = []

    for line in puzzle_input:
        chunks = set(line.rstrip(".").replace(",", "").split(" ")[4:])

        for word in (
            "a",
            "and",
            "generator",
            "microchip",
            "nothing",
            "relevant",
        ):
            chunks.discard(word)

        floors.append(chunks)

    floors[0].add("elevator")

    return floors


def move_objects(objects, floors, elevator, new_elevator):
    """Try to move given objects."""
    new_floors = copy.deepcopy(floors)
    new_floors[new_elevator].add("elevator")

    for object_ in objects:
        new_floors[elevator].remove(object_)
        new_floors[new_elevator].add(object_)

    if check_safety(frozenset(new_floors[new_elevator])) and check_safety(
        frozenset(new_floors[elevator])
    ):
        return [new_floors]

    return []


def perform_step(paths, best_paths):
    """Perform all legal steps."""
    floors, step = paths.popleft()
    step += 1
    moves = []

    for i, floor in enumerate(floors):
        if "elevator" in floor:
            floor.remove("elevator")
            objects = floor
            elevator = i
            break

    new_elevators = []

    if elevator != 0 and sum(len(floor) for floor in floors[:elevator]):
        new_elevators.append(elevator - 1)

    if elevator != len(floors) - 1:
        new_elevators.append(elevator + 1)

    for new_elevator in new_elevators:
        if len(objects) == 1:
            moves.extend(
                move_objects(
                    [next(iter(objects))], floors, elevator, new_elevator
                )
            )
            continue

        for object_ in objects:
            moves.extend(
                move_objects([object_], floors, elevator, new_elevator)
            )

        for object_0, object_1 in itertools.combinations(objects, 2):
            moves.extend(
                move_objects(
                    [object_0, object_1], floors, elevator, new_elevator
                )
            )

    for move in moves:
        if step < best_paths.get(floors_to_tuple(move), float("inf")):
            paths.append((move, step))
            best_paths[floors_to_tuple(move)] = step

    return paths, best_paths


if __name__ == "__main__":
    main()
