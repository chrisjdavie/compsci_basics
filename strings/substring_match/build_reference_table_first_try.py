from collections import deque
import unittest


class Test(unittest.TestCase):

    def test(self):

        substring = "ABABAC"
        table_expected = [[1,1,3,1,5,1],
                          [0,2,0,4,0,4],
                          [0,0,0,0,0,6]]
        table = build_table(substring)
        #for row in table:
        #    print(row)
        self.assertEqual(table, table_expected)


def build_table(substring):
    chrs_unique = sorted(set(substring))
    prior_references = { ref: deque() for ref in chrs_unique }
    table = [ [] for _ in chrs_unique ]

    for i, target in enumerate(substring):
        for j, c_un in enumerate(chrs_unique):
            if c_un == target:
                table[j].append(i+1)
                prior_references[c_un].appendleft(i+1)
            else:
                table[j].append(0)
                for poss_ind in prior_references[c_un]:
                    for k in range(1, poss_ind):
                        if substring[poss_ind-1-k] != substring[i-k]:
                            break
                    else:
                        table[j][-1] = poss_ind
                        break

    return table
