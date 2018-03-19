import unittest
from parameterized import parameterized

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", 2, True),
        ("provided example 1", 4, True),
        ("start num 0", 0, False),
        ("start num 1", 1, False),
        ("start num 3", 3, False),
        ("start num 5", 5, False),
        ("start num 6", 6, True),
        ("start num 7", 7, False),
        ("start num 8", 8, True),
        ("start num 9", 9, False),
        ("start num 3745", 3745, False)
    ])
    def test(self, _, start_num, expected_winner):
        self.assertEqual(play(start_num), expected_winner)


def play(start_num):
    """You choose number N. Tom and Jerry will play the game alternatively and
       each of them would subtract a number n [n< N] such that N%n=0. The game
       is repeated turn by turn until the one,who now cannot make a further 
       move looses the game. The game begins with Tom playing first move.
        
       True if you can win with start_num"""
    if start_num < 1:
        return False
    return not start_num%2
