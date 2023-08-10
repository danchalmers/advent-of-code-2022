from typing import Iterable


def day_ten():
    with open("data/input/day_ten.txt", "r") as f:
        lines = f.readlines()
    signal_sum = part_one(lines)
    print(f"day ten part one {signal_sum}")


def generate_x_states(lines: list[str]) -> list[int]:
    return list(_run_program(lines))


def part_one(lines: list[str]) -> int:
    return sum(part_one_generator(lines))

def part_one_generator(lines: list[str]) -> Iterable[int]:
    for idx, x in enumerate(_run_program(lines), start=1):
        if idx in [20, 60, 100, 140, 180, 220]:
            yield x * idx


def _run_program(lines: list[str]) -> Iterable[int]:
    x = 1
    for line in lines:
        command = line.split()[0]
        if command == "noop":
            yield x
        elif command == "addx":
            arg = int(line.split()[1])
            yield x
            yield x
            x = x + arg
    yield x
