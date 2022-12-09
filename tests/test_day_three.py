import pytest

from advent_of_code_2022.day_three import line_priority, total_priorities, group_priority, batch_lines, \
    total_group_priorities

EXAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

EXAMPLE_PRIORITIES = [16, 38, 42, 22, 20, 19]

EXAMPLE_GROUP_BADGES = [18, 52]

EXAMPLE_LINES_PRIORITIES = zip(
    [l for l in EXAMPLE_INPUT.splitlines() if len(l) > 0],
    EXAMPLE_PRIORITIES
)

EXAMPLE_GROUPS_PRIORITIES = zip(
    batch_lines(EXAMPLE_INPUT.splitlines()),
    EXAMPLE_GROUP_BADGES
)

@pytest.mark.parametrize("test_input, expected", EXAMPLE_LINES_PRIORITIES)
def test_item_twice_priority(test_input, expected):
    assert line_priority(test_input) == expected


def test_day_three_part_one():
    assert total_priorities(EXAMPLE_INPUT.splitlines()) == 157


@pytest.mark.parametrize("test_input, expected", EXAMPLE_GROUPS_PRIORITIES)
def test_day_three_group_priority(test_input, expected):
    assert group_priority(test_input) == expected

def test_day_three_part_two():
    assert total_group_priorities(EXAMPLE_INPUT.splitlines()) == 70
