"""
This is a very basic implementation of a heap, there are a bunch of
optimizations I've not done.

The Python stblib version (at the time of writing) is here. It is really
interesting to read

https://github.com/python/cpython/blob/3.6/Lib/heapq.py
"""

# TODO - duplicate values in push?

class MinHeap:

    def __init__(self, data):
        self.data = data

    def push(self, value):
        self.data.append(value)
        l_child = len(self.data) - 1
        l_parent = (l_child - 1)//2
        
        while l_child:
            if self.data[l_parent] <= self.data[l_child]:
                break
            self.data[l_child], self.data[l_parent] = self.data[l_parent], self.data[l_child]
            l_child = l_parent
            l_parent = (l_child - 1)//2

    def heapify(self):
        """There's an optimization that can be done here - """
        old_data = self.data
        self.data = []
        for value in old_data:
            self.push(value)

    def pop(self):
        if len(self.data) == 1:
            return self.data.pop()

        # pull a value up from the last point in the heap
        return_value = self.data[0]
        self.data[0] = self.data.pop()

        # bubble last value up
        pos = 0
        end_pos = len(self.data)
        child_pos = pos*2 + 1

        while child_pos < end_pos:
            # check if value is in correct position, stop if it is
            value = self.data[pos]
            right_child_pos = child_pos + 1
            if value <= self.data[child_pos] and (right_child_pos >= end_pos or value <= self.data[right_child_pos]):
                break
            # find smallest child to replace value with
            if right_child_pos < end_pos and self.data[right_child_pos] < self.data[child_pos]:
                child_pos = right_child_pos
            self.data[pos], self.data[child_pos] = self.data[child_pos], self.data[pos]
            pos = child_pos
            child_pos = pos*2 + 1

        return return_value


class HeapFactory:

    min_heap = MinHeap

    @classmethod
    def min_heap_from_unordered_data(cls, data):
        new_heap = cls.min_heap(data)
        new_heap.heapify()
        return new_heap

