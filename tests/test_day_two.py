from advent_of_code_2022.day_two import (
    score_with_part_one_strategy,
    day_two_part_one,
    score_with_part_two_strategy,
    day_two_part_two,
)

EXAMPLE_INPUT = """
A Y
B X
C Z
"""


def test_day_two_part_one():
    assert score_with_part_one_strategy(EXAMPLE_INPUT.splitlines()) == 15


def test_day_two_part_one_input():
    assert day_two_part_one() == 14375


def test_day_two_part_two():
    assert score_with_part_two_strategy(EXAMPLE_INPUT.splitlines()) == 12


def test_day_two_part_two_input():
    assert day_two_part_two() == 10274
