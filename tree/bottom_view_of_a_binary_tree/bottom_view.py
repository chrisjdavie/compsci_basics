class BottomViewData:
    """List functionality using a negative indexed list. 

    An over-complicated way of avoiding sorting, to keep the algo to O(N)"""

    def __init__(self, len_data):
        self._len_data = len_data
        self._data = [None]*(2*len_data-1)

    def _key_zeroed(self, key):
        return self._len_data-1+key

    def __setitem__(self, key, depth_val):
        key_z = self._key_zeroed(key)
        if self._data[key_z] is None or self._data[key_z][0] <= depth_val[0]:
            self._data[self._len_data-1+key] = depth_val

    def __getitem__(self, key):
        return self._data[self._key_zeroed(key)]

    def view(self):
        return [ item[1] for item in self._data if item is not None ]
