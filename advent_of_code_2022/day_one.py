from typing import Iterator


def day_one():
    with open("data/input/day_one.txt", "r") as f:
        print(f"day one part one: {most_calories_of_elves(f.readlines())}")
        f.seek(0)
        print(f"day one part two: {top_three_elves_calories(f.readlines())}")


def most_calories_of_elves(input_lines: Iterator[str]):
    return max(sum_blank_line_separated_groups(input_lines))


def top_three_elves_calories(input_lines: Iterator[str]):
    return sum(sorted(sum_blank_line_separated_groups(input_lines))[-3:])


def sum_blank_line_separated_groups(input_lines: Iterator[str]):
    elf_total = 0
    for line in input_lines:
        if len(line.strip()) == 0:
            yield elf_total
            elf_total = 0
        else:
            elf_total += int(line)
    yield elf_total
