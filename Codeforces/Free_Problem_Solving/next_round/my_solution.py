# https://codeforces.com/problemset/problem/158/A


def is_next_round(arr, index, n):
    for element in arr:
        if element < arr[index] or not element:
            n -= 1
    
    return n



n,k = map(int, input().split())
scores = [int(x) for x in input().split()]
print(is_next_round(scores, k-1, n))