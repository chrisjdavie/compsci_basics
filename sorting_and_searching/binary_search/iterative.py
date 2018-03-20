import unittest
from parameterized import parameterized


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 10, 8, 10, 25, 2),
        ("provided example 1", 10, 8, 10, 30, 2),
        ("provided example 2", 10, 8, 10, 12, 2),
        ("failed test", 12, 3, 9, 12, 2),
        ("linear wins", 1000, 1, 1, 1, 1),
        ("draw", 7, 2, 1, 1, 0)
        ])
    def test(self, _, length, target_index, linear_operation_time, binary_operation_time, expected_winner):
        self.assertEqual(binary_search_contest(length, target_index, linear_operation_time, binary_operation_time), expected_winner) 


def calc_num_ops_binary_search(length, target_index):

    start = 1
    end = length
    for num_binary_ops in range(length + 1):
        midpoint = (end + start)//2
        if midpoint == target_index:
            break

        if target_index > midpoint:
            start = midpoint + 1
        else:
            end = midpoint - 1

    return num_binary_ops + 1


def binary_search_contest(length, target_index, linear_operation_time, binary_operation_time):
    """Return 1 if linear search is faster than binary, return 2 if binary search is faster 
    than linear, return 0 if they are the same speed"""

    total_linear_time = target_index*linear_operation_time
    total_binary_time = calc_num_ops_binary_search(length, target_index)*binary_operation_time

    if total_linear_time == total_binary_time:
        return 0
    if total_linear_time < total_binary_time:
        return 1
    return 2
