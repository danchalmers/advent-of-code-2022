from typing import Iterator


Play = str


def day_two_part_one():
    with open("data/input/day_two.txt", "r") as f:
        score = score_with_part_one_strategy(f.readlines())
        print(f"day two part one: {score}")
        return score


def day_two_part_two():
    with open("data/input/day_two.txt", "r") as f:
        score = score_with_part_two_strategy(f.readlines())
        print(f"day two part two: {score}")
        return score


def score_with_part_one_strategy(input_lines: Iterator[str]):
    return sum(
        [score_strategy_line(part_one_generate_play(line)) for line in input_lines if line]
    )


def score_with_part_two_strategy(input_lines: Iterator[str]):
    return sum(
        [score_strategy_line(part_two_generate_play(line)) for line in input_lines if line]
    )


def part_one_generate_play(line: str) -> tuple[Play, Play]:
    other_play, my_play = line.split()
    match my_play:
        case ("X"):
            return other_play, "A"
        case ("Y"):
            return other_play, "B"
        case ("Z"):
            return other_play, "C"


def part_two_generate_play(line: str) -> tuple[Play, Play]:
    other_play, my_play = line.split()
    match (other_play, my_play):
        case (_, "Y"):
            return other_play, other_play
        case ("A", "X"):
            return other_play, "C"
        case ("A", "Z"):
            return other_play, "B"
        case ("B", "X"):
            return other_play, "A"
        case ("B", "Z"):
            return other_play, "C"
        case ("C", "X"):
            return other_play, "B"
        case ("C", "Z"):
            return other_play, "A"


def score_strategy_line(other_play_my_play: tuple[Play, Play]):
    other_play, my_play = other_play_my_play
    score = 0
    match my_play:
        case ("A"):
            score = 1
        case ("B"):
            score = 2
        case ("C"):
            score = 3
    if other_play == my_play:
        score += 3
    else:
        match (other_play, my_play):
            case ["C", "A"]:
                score += 6
            case ["B", "C"]:
                score += 6
            case ["A", "B"]:
                score += 6
    return score
