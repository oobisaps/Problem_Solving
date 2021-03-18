# https://codeforces.com/problemset/problem/282/A

def parse_operations(array):
    x = 0
    for operation in array:
        if '++' in operation:
            x += 1
        else: 
            x -= 1
    
    return x

n = int(input())
array_of_operations = []
for i in range(n):
    array_of_operations.append(input())


print(parse_operations(array_of_operations))