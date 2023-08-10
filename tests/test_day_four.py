from advent_of_code_2022.day_four import count_fully_contained, Range, count_overlaps

EXAMPLE_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

FIRST_LINES = """
43-62,63-68
49-81,85-97
52-77,52-78
9-62,49-62
28-92,29-92
79-80,75-80
3-98,2-99
16-87,17-94
16-25,24-29
11-86,85-87
"""


def test_contains_fully_b_inside():
    a = Range(2, 5)
    b = Range(3, 4)
    assert a.contains(b)

def test_contains_fully_a_inside():
    a = Range(3, 4)
    b = Range(2, 5)
    assert a.contains(b)

def test_contains_fully_b_inside_edge_aligned():
    a = Range(2, 5)
    b = Range(2, 4)
    assert a.contains(b)

def test_contains_fully_a_inside_edge_aligned():
    a = Range(3, 4)
    b = Range(4, 4)
    assert a.contains(b)

def test_not_contains_just_overlaps():
    a = Range(3, 5)
    b = Range(2, 4)
    assert not a.contains(b)


def test_not_contains_outside():
    a = Range(5, 6)
    b = Range(2, 4)
    assert not a.contains(b)


def test_overlaps_fully_b_inside():
    a = Range(2, 5)
    b = Range(3, 4)
    assert a.overlaps(b)


def test_overlaps_fully_a_inside():
    a = Range(3, 4)
    b = Range(2, 5)
    assert a.overlaps(b)


def test_overlaps_fully_b_inside_edge_aligned():
    a = Range(2, 5)
    b = Range(2, 4)
    assert a.overlaps(b)


def test_overlaps_fully_a_inside_edge_aligned():
    a = Range(3, 4)
    b = Range(4, 4)
    assert a.overlaps(b)


def test_overlaps_a_lower_than_b():
    a = Range(3, 5)
    b = Range(4, 6)
    assert a.overlaps(b)


def test_overlaps_a_higher_than_b():
    a = Range(5, 7)
    b = Range(4, 6)
    assert a.overlaps(b)


def test_not_overlaps_outside():
    a = Range(5, 6)
    b = Range(2, 4)
    assert not a.overlaps(b)


def test_count_fully_contained_example():
    assert count_fully_contained(EXAMPLE_INPUT.splitlines()) == 2


def test_count_fully_contained_ten_lines():
    assert count_fully_contained(FIRST_LINES.splitlines()) == 5


def test_count_overlaps_example():
    assert count_overlaps(EXAMPLE_INPUT.splitlines()) == 4
