# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def calc_fib_fast(n):

    if n<=1:
        return n

    previous, current = (0,1)

    for _ in range(1,n):
        previous, current = current, previous + current
    return current


def get_fib_period(m):
    previous, current = (0,1)
    
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        
        if previous == 0 and current == 1:
            return i + 1



def get_fibonacci_huge_fast(n, m):
    remainder = n % get_fib_period(m)

    return calc_fib_fast(remainder) % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))

