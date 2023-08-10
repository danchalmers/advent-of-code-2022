from advent_of_code_2022.day_five import top_of_stacks_9000, top_of_stacks_9001, clean_parse_stacks

EXAMPLE_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_initial_stacks():
    stacks, remaining = clean_parse_stacks(EXAMPLE_INPUT.splitlines())
    assert len(stacks) == 3
    assert len(stacks.get(1, [])) == 2
    assert len(stacks.get(2, [])) == 3
    assert len(stacks.get(3, [])) == 1


def test_day_five_part_one():
    assert top_of_stacks_9000(EXAMPLE_INPUT.splitlines()) == "CMZ"

def test_day_five_part_two():
    assert top_of_stacks_9001(EXAMPLE_INPUT.splitlines()) == "MCD"
