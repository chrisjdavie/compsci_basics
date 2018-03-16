from parameterized import parameterized
import unittest

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example", [(1, 4), (2, 4), (3,1)], 3, 3),
        ("nothing fits", [(5, 5),], 2, 0),
        ("one item", [(4, 4),], 4, 4),
        ("one item, space left", [(4, 4),], 5, 4),        
        ("two items, both valid", [(4, 4), (6, 3)], 4, 6),        
        ("two items, one valid", [(3, 4), (6, 5)], 4, 3),        
        ("two items, both fit", [(3, 1), (6, 2)], 4, 9),        
    ])
    def test(self, _, items, weight_limit, expected_value):
        self.assertEqual(fill_knapsack(items, weight_limit), expected_value)


class KnapsackItem:
    
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class BestKnapsack:

    def __init__(self, weight_limit):
        self._weight_limit = weight_limit
        self.best_value = -1

    def set_if_best(self, value, weight):
        if weight <= self._weight_limit and value > self.best_value:
            self.best_value = value


def _fill_knapsack(val_so_far, weight_so_far, n, best_knapsack, items, max_weight):
    if weight_so_far > max_weight:
        return
    best_knapsack.set_if_best(val_so_far, weight_so_far)
    if n < 1:
        return

    _fill_knapsack(val_so_far + items[n-1].value, weight_so_far + items[n-1].weight, n-1, best_knapsack, items, max_weight)
    _fill_knapsack(val_so_far, weight_so_far, n-1, best_knapsack, items, max_weight)


def fill_knapsack(raw_items, weight_limit):
    items = [ KnapsackItem(*ri) for ri in raw_items ]
    best_knapsack = BestKnapsack(weight_limit)

    _fill_knapsack(0, 0, len(items), best_knapsack, items, weight_limit)

    return best_knapsack.best_value
