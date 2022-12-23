import pytest

from advent_of_code_2022.day_eight import build_map, is_visible, count_visible_trees

EXAMPLE_INPUT = """30373
25512
65332
33549
35390
"""


@pytest.fixture(scope="module")
def example_trees():
    return build_map(EXAMPLE_INPUT.splitlines())


def test_1_1(example_trees):
    assert is_visible(example_trees, 1, 1)


def test_1_2(example_trees):
    assert is_visible(example_trees, 1, 2)


def test_1_3(example_trees):
    assert is_visible(example_trees, 1, 3) == False


def test_2_1(example_trees):
    assert is_visible(example_trees, 2, 1)


def test_2_2(example_trees):
    assert is_visible(example_trees, 2, 2) == False

def test_2_3(example_trees):
    assert is_visible(example_trees, 2, 3)


def test_3_2(example_trees):
    assert is_visible(example_trees, 3, 2)


def test_part_one():
    assert count_visible_trees(EXAMPLE_INPUT.splitlines()) == 21
