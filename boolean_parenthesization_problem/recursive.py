from parameterized import parameterized
import unittest

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", "T|T&F^T", 4),
        ("provided example 1", "T^F|F", 2),
        ("single True", "T", 1),
        ("single False", "F", 0)
    ])
    def test(self, _, bool_string, num_ways_true):
        self.assertEqual(evaluate_statement(bool_string), num_ways_true)


def eval_and(t_lhs, f_lhs, t_rhs, f_rhs):
    return t_lhs*t_rhs, t_lhs*f_rhs + f_lhs*t_rhs + f_lhs*f_rhs


def eval_or(t_lhs, f_lhs, t_rhs, f_rhs):
    return t_lhs*t_rhs + t_lhs*f_rhs + f_lhs*t_rhs, f_lhs*f_rhs


def eval_xor(t_lhs, f_lhs, t_rhs, f_rhs):
    return t_lhs*f_rhs + f_lhs*t_rhs, t_lhs*t_rhs + f_lhs*f_rhs


operation_map = {
    '&': eval_and,
    '|': eval_or,
    '^': eval_xor
}


def _evaluate_statement(statement, ind_start, ind_end):
    if ind_start + 1 == ind_end:
        if statement[ind_start] == "T":
            return 1, 0
        else:
            return 0, 1

    total_true, total_false = 0, 0
    for i in range(ind_start+1,ind_end,2):
        t_lhs, f_lhs = _evaluate_statement(statement, ind_start, i)
        t_rhs, f_rhs = _evaluate_statement(statement, i+1, ind_end)
        operation = statement[i]
        evaluates_true, evaluates_false = operation_map[operation](
            t_lhs, f_lhs, t_rhs, f_rhs)
        total_true += evaluates_true
        total_false += evaluates_false

    return total_true, total_false


def evaluate_statement(statement):        

    return _evaluate_statement(statement, 0, len(statement))[0]
