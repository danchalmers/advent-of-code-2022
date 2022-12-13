def day_four():
    with open("data/input/day_four.txt", "r") as f:
        count = count_fully_contained(f.readlines())
        print(f"day four part one: {count}")
    with open("data/input/day_four.txt", "r") as f:
        count = count_overlaps(f.readlines())
        print(f"day four part two: {count}")


class Range():
    def __init__(self, x, y):
        x = int(x)
        y = int(y)
        self.x = min(x, y)
        self.y = max(x, y)

    @staticmethod
    def range_from_text(repr):
        a = repr.split('-')
        return Range(a[0], a[1])

    def contains(self, other):
        return (self.x >= other.x and self.y <= other.y) or \
               (other.x >= self.x and other.y <= self.y)

    def overlaps(self, other):
        return (self.x <= other.y and self.y >= other.x) or \
               (other.x <= self.y and other.y >= self.x)


def count_fully_contained(lines: list[str]) -> int:
    return sum([a.contains(b) for a, b in make_pairs(lines)])


def count_overlaps(lines: list[str]) -> int:
    return sum([a.overlaps(b) for a, b in make_pairs(lines)])


def make_pairs(lines: list[str]) -> list[tuple[Range, Range]]:
    return [make_pair(line) for line in lines if len(line) > 0]


def make_pair(line: str) -> tuple[Range, Range]:
    pair = line.split(',')
    a = Range.range_from_text(pair[0])
    b = Range.range_from_text(pair[1])
    return a, b

