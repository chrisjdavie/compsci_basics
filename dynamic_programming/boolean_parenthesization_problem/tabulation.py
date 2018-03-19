from parameterized import parameterized
import unittest

class Test(unittest.TestCase):

    @parameterized.expand([
        ("provided example 0", "T|T&F^T", 4),
        ("provided example 1", "T^F|F", 2),
        ("single True", "T", 1),
        ("single False", "F", 0),
        ("failed provided test", "T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F", 638)
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


def evaluate_statement(statement):

    num_F_T = (len(statement) + 1)//2
    table = [ [None]*num_F_T for _ in range(num_F_T) ]

    # initialise diagonal
    for i_TF, T_or_F in enumerate(statement[::2]):
        table[i_TF][i_TF] = (0, 1)
        if T_or_F == "T":
            table[i_TF][i_TF] = (1, 0)

    # populate table
    for j in range(num_F_T):
        for i in range(j-1, -1, -1):
            #print(i,j)
            total_true = 0
            total_false = 0
            for k_TF, k_statement in enumerate(range(2*i+1, 2*j+1, 2)):
                t_lhs, f_lhs = table[i][i+k_TF]
                t_rhs, f_rhs = table[i+k_TF+1][j]
                this_true, this_false = operation_map[statement[k_statement]](
                    t_lhs, f_lhs, t_rhs, f_rhs)
                total_true += this_true
                total_false += this_false

            table[i][j] = (total_true, total_false)

    return table[0][-1][0]%1003

