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


def binary_search_contest(length, target_index, linear_operation_time, binary_operation_time):
    return -1
