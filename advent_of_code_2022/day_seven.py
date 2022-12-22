from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Optional, Iterable


def day_seven():
    with open("data/input/day_seven.txt", "r") as f:
        lines = f.readlines()
    sum_small_files = day_seven_part_one(lines)
    print(f"day seven part one: {sum_small_files}")
    smallest_big_dir = day_seven_part_two(lines)
    print(f"day seven part two: {smallest_big_dir}")


def day_seven_part_one(input) -> int:
    root = FileSystem.parse(input)
    return sum([size for size in root.dir_sizes() if size <= 100000])


def day_seven_part_two(input) -> int:
    root = FileSystem.parse(input)
    free_space = 70000000 - root.size_of()
    space_needed = 30000000 - free_space
    return min([size for size in root.dir_sizes() if size >= space_needed])

class FileSystem(ABC):
    @staticmethod
    def parse(description_lines: list[str]):
        root = Directory('/')
        pwd = root
        getting_ls = False
        for line in description_lines:
            parts = line.split()
            command = parts[0] == "$"
            if command:
                getting_ls = False
                if parts[1] == "cd":
                    if parts[2] == "..":
                        pwd = pwd.parent
                    elif parts[2] == "/":
                        pwd = root
                    else:
                        pwd = pwd.contents[parts[2]]
                elif parts[1] == "ls":
                    getting_ls = True
            elif getting_ls:
                if parts[0] == "dir":
                    name = parts[1]
                    f = Directory(name, parent=pwd)
                    pwd.contents[name] = f
                else:
                    size = int(parts[0])
                    name = parts[1]
                    f = File(name, size)
                    pwd.contents[name] = f
        return root

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def size_of(self) -> int:
        ...

    @abstractmethod
    def find_in(self, search_for) -> Optional["FileSystem"]:
        ...


class Directory(FileSystem):
    def __init__(self, name: str, parent: str = '/'):
        self.name = name
        self.contents = {}
        self.parent = parent

    @lru_cache
    def size_of(self) -> int:
        return sum([f.size_of() for f in self.contents.values()])

    @lru_cache
    def dir_sizes(self) -> Iterable[int]:
        for file in self.contents.values():
            if isinstance(file, Directory):
                for s in file.dir_sizes():
                    yield s
        yield self.size_of()

    def find_in(self, search_for) -> Optional[FileSystem]:
        if search_for == self.name:
            return self
        else:
            for f in self.contents.values():
                result = f.find_in(search_for)
                if result is not None:
                    return result
            return None


class File(FileSystem):
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size

    def size_of(self):
        return self._size

    def find_in(self, search_for) -> Optional[FileSystem]:
        if search_for == self.name:
            return self
        else:
            return None
