import unittest
from bin_tree import gen_bin_tree


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(gen_bin_tree(), {'value': 7, 'left': {'value': 21, 'left': {'value': 63, 'left': {'value': 189, 'left': {'value': 567, 'left': {}, 'right': {}}, 'right': {'value': 185, 'left': {}, 'right': {}}}, 'right': {'value': 59, 'left': {'value': 177, 'left': {}, 'right': {}}, 'right': {'value': 55, 'left': {}, 'right': {}}}}, 'right': {'value': 17, 'left': {'value': 51, 'left': {'value': 153, 'left': {}, 'right': {}}, 'right': {'value': 47, 'left': {}, 'right': {}}}, 'right': {'value': 13, 'left': {'value': 39, 'left': {}, 'right': {}}, 'right': {'value': 9, 'left': {}, 'right': {}}}}}, 'right': {'value': 3, 'left': {'value': 9, 'left': {'value': 27, 'left': {'value': 81, 'left': {}, 'right': {}}, 'right': {'value': 23, 'left': {}, 'right': {}}}, 'right': {'value': 5, 'left': {'value': 15, 'left': {}, 'right': {}}, 'right': {'value': 1, 'left': {}, 'right': {}}}}, 'right': {'value': -1, 'left': {'value': -3, 'left': {'value': -9, 'left': {}, 'right': {}}, 'right': {'value': -7, 'left': {}, 'right': {}}}, 'right': {'value': -5, 'left': {'value': -15, 'left': {}, 'right': {}}, 'right': {'value': -9, 'left': {}, 'right': {}}}}}})
    def test2(self):
        self.assertEqual(gen_bin_tree(2, 10), {'value': 10, 'left': {'value': 30, 'left': {'value': 90, 'left': {}, 'right': {}}, 'right': {'value': 26, 'left': {}, 'right': {}}}, 'right': {'value': 6, 'left': {'value': 18, 'left': {}, 'right': {}}, 'right': {'value': 2, 'left': {}, 'right': {}}}})
    def test3(self):
        self.assertEqual(gen_bin_tree(2, 1, lambda x: x+1, lambda x: x-1), {'value': 1, 'left': {'value': 2, 'left': {'value': 3, 'left': {}, 'right': {}}, 'right': {'value': 1, 'left': {}, 'right': {}}}, 'right': {'value': 0, 'left': {'value': 1, 'left': {}, 'right': {}}, 'right': {'value': -1, 'left': {}, 'right': {}}}})


if __name__ == '__main__':
    unittest.main()