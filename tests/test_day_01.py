from aoc_23 import day_01
from aoc_23.load_data import get_test_data

test_data = get_test_data("01")
expected_result_part_1 = 347
expected_result_part_2 = 267

data_part_2_string_containing_multiple_numbers_crossover = "eightwothree"
expected_result_part_2_string_containing_multiple_numbers_crossover = 83


def test_part_1():
    assert day_01.part_1(test_data) == expected_result_part_1


def test_part_2():
    assert day_01.part_2(test_data) == expected_result_part_2


def test_part_2_string_containing_multiple_numbers_crossover():
    assert (
        day_01.part_2(data_part_2_string_containing_multiple_numbers_crossover)
        == expected_result_part_2_string_containing_multiple_numbers_crossover
    )
