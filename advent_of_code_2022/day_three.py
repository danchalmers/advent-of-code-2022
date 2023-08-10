def day_three():
    with open("data/input/day_three.txt", "r") as f:
        score = total_priorities(f.readlines())
        print(f"day three part one: {score}")
    with open("data/input/day_three.txt", "r") as f:
        score = total_group_priorities(f.readlines())
        print(f"day three part two: {score}")


def total_priorities(input_lines: list[str]) -> int:
    return sum([line_priority(line.strip()) for line in input_lines])


def total_group_priorities(input_lines: list[str]) -> int:
    return sum(group_priority(batch) for batch in batch_lines(input_lines))


def line_priority(input_line: str) -> int:
    if len(input_line) == 0:
        return 0
    side_item_count = len(input_line) // 2
    xs = set(input_line[:side_item_count])
    ys = set(input_line[side_item_count:])
    in_both = xs & ys
    return sum([char_priority(z) for z in in_both])


def group_priority(group_lines: list[str]) -> int:
    xs = set.intersection(*map(set, group_lines))
    return sum([char_priority(x) for x in xs])


def char_priority(x):
    y = ord(x)
    if y >= 97 and y <= 122:
        return y - 96
    elif y >= 65 and y <= 90:
        return y - 65 + 27
    else:
        print(f"unexpected input {x}")
        return 0


def batch_lines(lines):
    lines = [l.strip() for l in lines if len(l) > 0]
    for i in range(0, len(lines), 3):
        yield lines[i:i+3]
