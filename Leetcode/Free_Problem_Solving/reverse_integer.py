""""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

import math

class Solution:
    def reverse(self, x: int) -> int:

        reverse_x = 0
        negative_flag = False


        if x < 0:
            negative_flag = True
            x = x * (-1)

        i = 1
        number_of_digits =  int(math.log10(x)) + 1  

        while x:
            reverse_x += (x % 10)  * 10 ** (number_of_digits - i)
            x //= 10
            i += 1


        if negative_flag:
            return reverse_x * (-1)
        
        return reverse_x



        

test_counter = 0
solution_obj = Solution()
while True:
    try:
        test = int(input('input integer : '))
        test_counter += 1

        print(' Test {} : '.format(test_counter))
        print('Output {} : '.format(solution_obj.reverse(int(test))))

    except KeyboardInterrupt:
        print('Finish Testing')
        break


