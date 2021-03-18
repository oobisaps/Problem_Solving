from typing import List

class Solution:

    def findMaxConsecutiveOnes_solution_one(self, nums : List[int]) -> int:
        consecutive_temp, consecutive_max = (0, -1)
        for num in nums:
            if num:
                consecutive_temp += 1
            else:
                consecutive_temp = 0

            if consecutive_temp > consecutive_max:
                consecutive_max = consecutive_temp
        
        return consecutive_max
        
    


nums = [1,1,0,1,1,0,1,1,1,0]


solution = Solution()

solution_one_result = solution.findMaxConsecutiveOnes_solution_one(nums)

print(f"Solution one : {solution_one_result}")