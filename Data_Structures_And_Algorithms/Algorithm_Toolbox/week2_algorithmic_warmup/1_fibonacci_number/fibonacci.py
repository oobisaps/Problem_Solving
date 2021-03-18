# 0 1 1 2 3 5 8

# from helpers import stress_test

# Uses python3
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)


def calc_fib_fast_V1(n):
    fib_numbers = [0,1]

    for i in range(2,n + 1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    
    return fib_numbers[-1]

def calc_fib_fast_V2(n):

    if n<=1:
        return n

    fib_num = 0
    fib_first, fib_second = (0,1)

    for _ in range(1,n):
        fib_num = fib_first + fib_second
        fib_first = fib_second
        fib_second = fib_num

    return fib_num

n = int(input())
# print(calc_fib_naive(n))
# print(calc_fib_fast_V1(n))
print(calc_fib_fast_V2(n))
