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

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == self.reverse(x):
            return True
        
        return False


test_counter = 0
solution_obj = Solution()
while True:
    try:
        test = int(input('input integer : '))
        test_counter += 1

        print(' Test {} : '.format(test_counter))
        print(' Output {} : '.format(solution_obj.isPalindrome(test)))

    except KeyboardInterrupt:
        print('Finish Testing')
        break