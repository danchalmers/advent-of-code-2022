"""
I'm aiming at basic python, as a constraint.
There's a solution with numpy that I'm deliberately ignoring :)
"""

Map = list[list[int]]
VisibleMap = list[list[bool]]


def day_eight():
    with open("data/input/day_eight.txt", "r") as f:
        lines = f.readlines()
    visible_trees = count_visible_trees(lines)
    print(f"day eight part one {visible_trees}")


def count_visible_trees(input_lines: list[str]) -> int:
    visible_map = build_map(input_lines)
    return sum([1 if z else 0 for row in visible_map for z in row])



def visible_on_row(map: Map, visible_map: VisibleMap, forward: bool) -> VisibleMap:
    rows, cols, start, end, step = _visible_on_start(map, forward)
    if forward:
        end = cols
    else:
        start = cols - 1
    for row in range(rows):
        max_so_far = -1
        for col in range(start, end, step):
            visible_map, max_so_far = _visible_on_inner(visible_map, map, max_so_far, row, col)
    return visible_map


def visible_on_col(map: Map, visible_map: VisibleMap, forward: bool) -> VisibleMap:
    rows, cols, start, end, step = _visible_on_start(map, forward)
    if forward:
        end = rows
    else:
        start = rows - 1
    for col in range(cols):
        max_so_far = -1
        for row in range(start, end, step):
            visible_map, max_so_far = _visible_on_inner(visible_map, map, max_so_far, row, col)
    return visible_map


def _visible_on_start(map: Map, forward: bool):
    rows = len(map)
    cols = len(map[0])
    if forward:
        start = 0
        end = None
        step = 1
    else:
        start = None
        end = -1
        step = -1
    return rows, cols, start, end, step


def _visible_on_inner(visible_map, map, max_so_far, row, col):
    visible_map[row][col] = visible_map[row][col] or (map[row][col] > max_so_far)
    max_so_far = max(max_so_far, map[row][col])
    return visible_map, max_so_far


def build_map(input_lines: list[str]) -> VisibleMap:
    map = [[int(z) for z in line.strip()] for line in input_lines]
    visible_map = [[False for col in row] for row in map]
    visible_map = visible_on_row(map, visible_map, True)
    visible_map = visible_on_row(map, visible_map, False)
    visible_map = visible_on_col(map, visible_map, True)
    visible_map = visible_on_col(map, visible_map, False)
    return visible_map


def is_visible(visible_map: VisibleMap, row: int, col: int) -> bool:
    return visible_map[row][col]

