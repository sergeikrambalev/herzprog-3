import unittest

def add(data, target):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == target:
                return [i, j]


class AddTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(add([2, 7, 11, 15], 9), [0, 1])
    def test2(self):
        self.assertEqual(add([3, 2, 4], 6), [1, 2])
    def test3(self):
        self.assertEqual(add([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()

