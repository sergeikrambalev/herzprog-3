import unittest
from bin_tree import gen_bin_tree


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(gen_bin_tree(), {'value': 7, 'left': {'value': 21, 'left': {'value': 63, 'left': {'value': 189, 'left': {'value': 567}, 'right': {'value': 185}}, 'right': {'value': 59, 'left': {'value': 177}, 'right': {'value': 55}}}, 'right': {'value': 17, 'left': {'value': 51, 'left': {'value': 153}, 'right': {'value': 47}}, 'right': {'value': 13, 'left': {'value': 39}, 'right': {'value': 9}}}}, 'right': {'value': 3, 'left': {'value': 9, 'left': {'value': 27, 'left': {'value': 81}, 'right': {'value': 23}}, 'right': {'value': 5, 'left': {'value': 15}, 'right': {'value': 1}}}, 'right': {'value': -1, 'left': {'value': -3, 'left': {'value': -9}, 'right': {'value': -7}}, 'right': {'value': -5, 'left': {'value': -15}, 'right': {'value': -9}}}}})
    def test2(self):
        self.assertEqual(gen_bin_tree(2, 10), {'value': 10, 'left': {'value': 30, 'left': {'value': 90}, 'right': {'value': 26}}, 'right': {'value': 6, 'left': {'value': 18}, 'right': {'value': 2}}})
    def test3(self):
        self.assertEqual(gen_bin_tree(2, 1, lambda x: x+1, lambda x: x-1), {'value': 1, 'left': {'value': 2, 'left': {'value': 3}, 'right': {'value': 1}}, 'right': {'value': 0, 'left': {'value': 1}, 'right': {'value': -1}}})


if __name__ == '__main__':
    unittest.main()