import unittest
from parameterized import parameterized


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 10, 8, 10, 25, 2),
        ("provided example 1", 10, 8, 10, 30, 2),
        ("provided example 2", 10, 8, 10, 12, 2),
        ("linear wins", 1000, 1, 1, 1, 1),
        ("draw", 5, 2, 1, 1, 0)
        ])
    def test(self, _, length, target_index, linear_operation_time, binary_operation_time, expected_winner):
        self.assertEqual(binary_search_contest(length, target_index, linear_operation_time, binary_operation_time), expected_winner) 


def calc_num_ops_binary_search(length, target_index):

    start = 1
    end = length
    for num_binary_ops in range(length + 1):
        midpoint = (end + start + 1)//2
        if midpoint == target_index:
            break

        if target_index > midpoint:
            start = midpoint
        else:
            end = midpoint

    return num_binary_ops + 1


def binary_search_contest(length, target_index, linear_operation_time, binary_operation_time):

    total_linear_time = target_index*linear_operation_time
    total_binary_time = calc_num_ops_binary_search(length, target_index)*binary_operation_time

    if total_linear_time == total_binary_time:
        return 0
    if total_linear_time < total_binary_time:
        return 1
    return 2
