import unittest


class Test(unittest.TestCase):

    def test(self):

        substring = "ABABAC"
        table_expected = [[1,1,3,1,5,1],
                          [0,2,0,4,0,4],
                          [0,0,0,0,0,6]]
        table = build_table(substring)
        for row in table:
            print(row)
        self.assertEqual(table, table_expected)


def build_table(substring):
    chrs_unique = sorted(set(substring))
    table = [ [] for _ in chrs_unique ]

    # initialisation of 0
    target = substring[0]
    for ch_un, row in zip(chrs_unique, table):
        row.append(0)
        if ch_un == target:
            row[-1] = 1

    x = 0
    for j, target in enumerate(substring[1:], 1):        
        for ch_un, row in zip(chrs_unique, table):
            row.append(row[x])
        table[chrs_unique.index(target)][-1] = j+1
        x = table[chrs_unique.index(target)][x]
    return table
