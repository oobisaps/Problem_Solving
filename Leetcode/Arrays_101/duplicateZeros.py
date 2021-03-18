from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)

        while i < n:
            if not arr[i]:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i+=1

            
                

        print(arr)

arr = [1,0,2,3,0,4,5,0]
print(arr)
solution = Solution()

solution.duplicateZeros(arr)