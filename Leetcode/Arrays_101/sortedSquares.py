from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([num**2 for num in A])


nums = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(nums))