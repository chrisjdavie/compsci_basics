"""
Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1.

https://practice.geeksforgeeks.org/problems/next-larger-element/0
"""
from parameterized import parameterized
import unittest


class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [1, 3, 2, 4], [3, 4, 4, -1]),
        ("provided example 1", [4, 5, 2, 25], [5, 25, 25, -1])
    ])
    def test(self, _, input_arr, expected_output):
        self.assertEqual(next_greater_element(input_arr), expected_output)


def next_greater_element(arr):
    return -1

