# https://codeforces.com/problemset/problem/4/A

def even_watermelon(n):
    if n%2 == 0 and  n > 2:
        print('YES')
    else:
        print('NO')
 
 
n = int(input()) 
even_watermelon(n)