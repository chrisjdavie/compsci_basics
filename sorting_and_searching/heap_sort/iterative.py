"""This is an attempt following the recipies of other people - my first attempt
(in 'old') had the right O in time but wasn't in-place. Also too longer than
the more proper versions.
"""
import copy
import unittest

from parameterized import parameterized


class TestMaxHeap(unittest.TestCase):

    @parameterized.expand([
        ([3, 5, 7, 1, 8, 6, 2, 4],),
    ])
    def test_heapify(self, arr):
        heap = MaxHeap(arr)
        heap.heapify()
        for pos, value in enumerate(arr[:len(arr)//2]):
            pos_l_child = 2*pos + 1
            pos_r_child = 2*pos + 2
            self.assertLessEqual(heap.data[pos_l_child], value)
            if pos_r_child < len(arr):
                self.assertLessEqual(heap.data[pos_r_child], value)
        print(heap.data)


class TestHeapSort(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", [5, 1, 4, 2, 8]),
        ("provided example 1", [3, 1]),
        ("provided example 2", [4, 1, 3, 9, 7]),
        ("provided example 3", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ("provided example 4", [4, 3, 2, 10, 12, 1, 5, 6]),
        ("provided example 5", [12, 11, 13, 5, 6]),
        ("single value", [5]),
        ("already sorted", [1, 3, 8])
    ])
    def test(self, _, arr):
        heap = MaxHeap(arr)
        heap.heapify()
        sorted_arr = sorted(arr)
        heap_sort(arr)
        self.assertEqual(sorted_arr, arr)


def heap_sort(arr):
    heap = MaxHeap(arr)
    for end_pos in range(len(arr)-1, 0, -1):
        largest = heap.pushpop(heap.data[end_pos], end_pos)
        arr[end_pos] = largest


class MaxHeap:

    def __init__(self, data):
        self.data = data

    def heapify(self):
        for pos in range(len(self.data)//2-1, -1, -1):
            self._sift(pos, len(self.data))

    def pushpop(self, value, end_pos):
        pop_value = self.data[0]
        self.data[0] = value
        self._sift(0, end_pos)
        return pop_value

    def _sift(self, pos, end_pos):
        child_pos = 2*pos + 1
        while child_pos < end_pos:
            child_pos_right = child_pos + 1
            # stop if the heap constraint is satisfied
            if self.data[pos] >= self.data[child_pos] and (child_pos_right >= end_pos or self.data[pos] >= self.data[child_pos_right]):
                break
            # find the greatest child, use that
            if child_pos_right < end_pos and self.data[child_pos_right] > self.data[child_pos]:
                child_pos = child_pos_right
            # swap child for parent
            self.data[pos], self.data[child_pos] = self.data[child_pos], self.data[pos]
            # set new indices
            pos = child_pos
            child_pos = pos*2 + 1
