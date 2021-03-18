import math
from typing import List


class Solution:
    def findNumbers_solution_one(self, nums: List[int]) -> int:
        return sum([1 for i in nums if len(str(i)) % 2 == 0])
    
    def findNumbers_solution_two(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            if (int(math.log10(num)) + 1) % 2 == 0:
                counter += 1
        
        return counter
