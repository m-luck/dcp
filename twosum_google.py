import unittest
from typing import List

def two_sum(nums: List[int], k):
    cache = { num for num in nums }
    for num in nums:
        if k - num in cache:
            return True
    return False

class TestTwoSum(unittest.TestCase):

    def test_1(self):
        inp = [10, 15, 3, 7]
        self.assertTrue(two_sum(inp, 17))

if __name__ == "__main__":
    unittest.main()