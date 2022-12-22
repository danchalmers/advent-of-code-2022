import pytest

from advent_of_code_2022.day_six import start_position_in_signal

EXAMPLE_RESULTS_PART_1 = [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]

EXAMPLE_RESULTS_PART_2 = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg",  23),
     ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
     ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]

@pytest.mark.parametrize("signal, position", EXAMPLE_RESULTS_PART_1)
def test_start_marker_position(signal, position):
    assert start_position_in_signal(signal, 4) == position

@pytest.mark.parametrize("signal, position", EXAMPLE_RESULTS_PART_2)
def test_start_marker_position(signal, position):
    assert start_position_in_signal(signal, 14) == position