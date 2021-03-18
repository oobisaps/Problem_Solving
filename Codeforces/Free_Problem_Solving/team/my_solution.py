# https://codeforces.com/problemset/problem/231/A

def team(matrix, n):
    for arr in matrix:
        if sum(arr) < 2:
            n -= 1
    
    return n

n = int(input())
matrix = []
for i in range(n):
    matrix.append(map(int, input().split()))


print(team(matrix, n))