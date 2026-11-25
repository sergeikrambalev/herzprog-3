import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_basic_case(self):
        result = add([2, 7, 11, 15], 9)
        self.assertIn(result, ([0, 1], [1, 0]))

    def test_no_pair_exists(self):
        result = add([1, 2, 3, 4], 100)
        self.assertIsNone(result)

    def test_empty_list(self):
        result = add([], 5)
        self.assertIsNone(result)

    def test_single_element(self):
        result = add([5], 5)
        self.assertIsNone(result)

    def test_two_elements_match(self):
        result = add([3, 7], 10)
        self.assertIn(result, ([0, 1], [1, 0]))

    def test_two_elements_no_match(self):
        result = add([3, 7], 11)
        self.assertIsNone(result)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, 4]
        result = add(nums, -4)
        self.assertIsNotNone(result)
        self.assertEqual(nums[result[0]] + nums[result[1]], -4)

    def test_duplicate_values(self):
        nums = [3, 3, 3]
        result = add(nums, 6)
        self.assertIsNotNone(result)
        self.assertNotEqual(result[0], result[1])
        self.assertEqual(nums[result[0]] + nums[result[1]], 6)

    def test_multiple_valid_pairs(self):
        nums = [1, 2, 3, 4, 5]
        result = add(nums, 6)
        self.assertIsNotNone(result)
        self.assertNotEqual(result[0], result[1])
        self.assertEqual(nums[result[0]] + nums[result[1]], 6)

    def test_zero_target(self):
        nums = [-3, 1, 2, 3]
        result = add(nums, 0)
        self.assertIsNotNone(result)
        self.assertEqual(nums[result[0]] + nums[result[1]], 0)

    def test_pair_at_the_end(self):
        result = add([1, 2, 3, 4, 5], 9)
        self.assertIn(result, ([3, 4], [4, 3]))

    def test_same_value_needed_twice(self):
        result = add([5, 1, 5], 10)
        self.assertIn(result, ([0, 2], [2, 0]))


if __name__ == "__main__":
    unittest.main()