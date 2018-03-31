from .heap import MinHeap
from parameterized import parameterized
import unittest

class TestHeap(unittest.TestCase):

    @parameterized.expand([
        ([], 1, [1]),
        ([3], 4, [3,4]),
        ([3], 2, [2,3]),
        ([1, 5, 3], 6, [1, 5, 3, 6]),
        ([1, 5, 3], 4, [1, 4, 3, 5]),
        ([1, 5, 3, 8, 6, 7], 4, [1, 5, 3, 8, 6, 7, 4])
    ])
    def test_push(self, data, value, resultant_heap):
        test_heap = MinHeap(data)
        test_heap.push(value)
        self.assertEqual(test_heap.data, resultant_heap)

    def test_heapify(self):
        data = [6, 7, 6, 1, 1]
        test_heap = MinHeap(data)
        test_heap.heapify()
        # test the heap relationship (the heap is deterministic, but
        # could be generated anyway that satisfies the relationship)
        for i, value_child in enumerate(test_heap.data[1:]):
            i_child = i + 1
            i_parent = (i_child - 1)//2
            self.assertLessEqual(test_heap.data[i_parent], value_child)

    @parameterized.expand([
        ([1, 5, 3, 8, 6, 7],),
        ([6, 5, 2, 1, 8, 7, 2, 4],),
        ([7, 8],)
    ])
    def test_pop(self, data):
        test_heap = MinHeap(data)
        test_heap.heapify()

        # min heaps pop in ascending order
        for value in sorted(data):
            self.assertEqual(test_heap.pop(), value)

