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


def fill_knapsack(raw_items, weight_limit):
    """You are given weights and values of items, put these items in a knapsack
       of capacity weight_limit to get the maximum total value in the knapsack."""
    table = [ [0]*(weight_limit+1) for _ in range(len(raw_items)) ]

    # initialise first row
    value_item = raw_items[0][0]
    weight_item = raw_items[0][1]
    for j in range(min([weight_item, weight_limit+1])):
        table[0][j] = 0
    for j in range(weight_item, weight_limit+1):
        table[0][j] = value_item

    for i, item in enumerate(raw_items[1:]):
        value_item = raw_items[i+1][0]
        weight_item = raw_items[i+1][1]
        for j in range(min([weight_item, weight_limit+1])):
            table[i+1][j] = table[i][j]
        for j in range(weight_item, weight_limit+1):
            table[i+1][j] = max([table[i][j], table[i][j-weight_item] + value_item])

    return table[-1][-1]
