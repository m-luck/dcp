import unittest
from typing import List

def pdp(nums: List):
    
    n = len(nums)
    if(n == 0): return []

    # Hold the 
    res = [1] * n

    # Scan left to right.
    for ind in range(1,n):
        res[ind] = nums[ind-1] * res[ind-1]

    running_r = 1

    # Scan right to left while ignoring rest of right.
    for ind in reversed(range(n)):
        res[ind] = res[ind] * running_r 
        running_r *= nums[ind]

    return res
    

class TestProd(unittest.TestCase):

    def test_1(self):
        L = [4,5,1,8,2]
        exp = [80,64,320,40,160]
        self.assertEqual(pdp(L), exp)
        
    def test_2(self):
        L = [1,2,3,4]
        exp = [24,12,8,6]
        self.assertEqual(pdp(L), exp)

if __name__ == "__main__":
    unittest.main()