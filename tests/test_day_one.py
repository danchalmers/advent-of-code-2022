from advent_of_code_2022.day_one import most_calories_of_elves, top_three_elves_calories

EXAMPLE_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_day_one_part_one():
    assert most_calories_of_elves(EXAMPLE_INPUT.splitlines()) == 24_000


def test_day_one_part_two():
    assert top_three_elves_calories(EXAMPLE_INPUT.splitlines()) == 45_000
