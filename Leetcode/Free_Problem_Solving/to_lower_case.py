'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"

Example 2:

Input: "here"
Output: "here"

Example 3:

Input: "LOVELY"
Output: "lovely"

'''


from string import ascii_lowercase
from string import ascii_uppercase

class Solution:
    def toLowerCase(self, str: str) -> str:
        hash_ = dict(zip(ascii_uppercase,ascii_lowercase))
        

        return ''.join((hash_[x] if x in hash_ else x for x in list(str)))

s = Solution()

while(1):
    str_ = input('The String : ')
    if str_ != 'stop':
        print(s.toLowerCase(str = str_))
    else:
        break