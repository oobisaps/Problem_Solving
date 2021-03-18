'''
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.


'''
import time
from functools import reduce
from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = Counter(S)

        start = time.time()
        version_1 = list(map(lambda x : x in J,S)).count(True) 
        total = time.time() - start
        print('Version_1 : time is {},output is {}'.format(total,version_1))
        print('')

        start = time.time()
        version_2 = len([i for i in list(S) if i in J])
        total = time.time() - start
        print('Version_2 : time is {},output is {}'.format(total,version_2))
        print('')

        start = time.time()
        version_3 = reduce(lambda x,y : c.get(x) + c.get(y),J) 
        total = time.time() - start
        print('Version_3 : time is {},output is {}'.format(total,version_3))
        print('')

s = Solution()

while(True):
    stones = input('The Stones : ')
    jewels = input('The Jewels : ')
    if stones == 'stop' or jewels == 'stop':
        break
    else:
        s.numJewelsInStones(J = jewels,S = stones)
    