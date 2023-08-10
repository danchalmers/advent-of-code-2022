import pytest

from advent_of_code_2022.day_seven import FileSystem, day_seven_part_one, day_seven_part_two

EXAMPLE_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


@pytest.fixture
def filesystem():
    return FileSystem.parse(EXAMPLE_INPUT.splitlines())

def test_size_of_h(filesystem):
    assert filesystem.find_in('h.lst').size_of() == 62596


def test_size_of_e(filesystem):
    assert filesystem.find_in('e').size_of() == 584


def test_size_of_a(filesystem):
    assert filesystem.find_in('a').size_of() == 94853


def test_size_of_d(filesystem):
    assert filesystem.find_in('d').size_of() == 24933642


def test_size_of_root(filesystem):
    assert filesystem.find_in('/').size_of() == 48381165


def test_part_one():
    assert day_seven_part_one(EXAMPLE_INPUT.splitlines()) == 95437


def test_part_two():
    size_of_dir_to_delete = day_seven_part_two(EXAMPLE_INPUT.splitlines())
    assert size_of_dir_to_delete >= 24933642
