# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast_1_max(numbers):
    max_value_1, max_value_2 = (0,0)
    
    for number in numbers:
        if number > max_value_1:
            max_value_2 = max_value_1
            max_value_1 = number
        elif number > max_value_2:
            max_value_2 = number
    
    return max_value_1 * max_value_2


def max_pairwise_product_fast_2_max(numbers):

    max_value_1_index, max_value_2_index = (0, 0)

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_value_1_index]:
            max_value_1_index = i

    if max_value_1_index == 0:
        max_value_2_index = 1

    for j in range(1, len(numbers)):
        if numbers[j] > numbers[max_value_2_index] and j != max_value_1_index:
            max_value_2_index = j


    return numbers[max_value_1_index] * numbers[max_value_2_index]        



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_fast_2_max(input_numbers))