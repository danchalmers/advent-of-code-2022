from collections import defaultdict

Stack = list[str]


def day_five():
    with open("data/input/day_five.txt", "r") as f:
        top_crates = top_of_stacks_9000(f.readlines())
        print(f"day five part one: {top_crates}")
        with open("data/input/day_five.txt", "r") as f:
            top_crates = top_of_stacks_9001(f.readlines())
            print(f"day five part two: {top_crates}")


def top_of_stacks_9000(lines: list[str]) -> str:
    stacks, moves = clean_parse_stacks(lines)
    return handle_moves(stacks, moves, True)


def top_of_stacks_9001(lines: list[str]) -> str:
    stacks, moves = clean_parse_stacks(lines)
    return handle_moves(stacks, moves, False)


def handle_moves(stacks: dict[int, Stack], moves: list[str], like_popping: bool) -> str:
    for move in moves:
        n, source, destination = parse_move(move)
        xs = stacks[source][n:]
        if like_popping:
            xs = list(reversed(xs))
        stacks[source] = stacks[source][:n]
        stacks[destination].extend(xs)
    return "".join([s[-1] for s in stacks.values()])


def clean_parse_stacks(lines: list[str]) -> tuple[dict[int, Stack], list[str]]:
    stacks, remaining = _parse_stacks(lines)
    return {
        idx: list(reversed([s for s in stack if s.isalpha()]))
        for idx, stack in stacks.items()
    }, remaining


def _parse_stacks(lines: list[str]) -> tuple[dict[int, Stack], list[str]]:
    stacks = defaultdict(list)
    for line_idx, line in enumerate(lines):
        if len(line.strip()) == 0:
            return stacks, lines[line_idx+1:]
        for column_id, chr_idx in enumerate(range(1, len(line), 4), start=1):
            stacks[column_id].append(line[chr_idx])
    return stacks, []


def parse_move(move) -> tuple[int, int, int]:
    parts = move.split()
    return -(int(parts[1])), int(parts[3]), int(parts[5])
