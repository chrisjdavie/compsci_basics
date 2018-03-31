from parameterized import parameterized
import unittest

from heap_sort.heap import HeapFactory

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ("provided example 1", [3, 1], [1, 3]),
        ("provided example 2", [4, 1, 3, 9, 7], [1, 3, 4, 7, 9]),
        ("provided example 3", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ("provided example 4", [4, 3, 2, 10, 12, 1, 5, 6], [1, 2, 3, 4, 5, 6, 10, 12]),
        ("provided example 5", [4, 3, 2, 10, 12, 1, 5, 6], [1, 2, 3, 4, 5, 6, 10, 12]),
        ("provided example 6", [12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
        ("single value", [5], [5]),
        ("already sorted", [1, 3, 8], [1, 3, 8])
    ])
    def test(self, _, arr, sorted_arr):
        self.assertEqual(heap_sort(arr), sorted_arr)


def heap_sort(arr):

    min_heap = HeapFactory.min_heap_from_unordered_data(arr)
    
    sorted_arr = []
    while min_heap.data:
        sorted_arr.append(min_heap.pop())
    
    return sorted_arr
