

test_case_1 = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]
]

test_case_2 = [
    [-1,1,-1,0,0,0],
    [0,-1,0,0,0,0],
    [-1,-1,-1,0,0,0],
    [0,-9,2,-4,-4,0],
    [-7,0,0,-2,0,0],
    [0,0,-1,-2,-4,0]
]

def hourglassSum(arr):
    max_sung_sum = -1e10

    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            curr_sung_sum = sum(arr[i][j:j+3])
            curr_sung_sum += arr[i+1][j+1]
            curr_sung_sum += sum(arr[i+2][j:j+3])


            if curr_sung_sum > max_sung_sum:
                max_sung_sum = curr_sung_sum
    
    return max_sung_sum
        
