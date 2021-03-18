# https://codeforces.com/problemset/problem/263/A

def make_beutiful_matrix(ugly_eye):
    beautiful_eye = (2,2)
    return abs(beautiful_eye[0] - ugly_eye[0]) + abs(beautiful_eye[1] - ugly_eye[1])


eye_position = (0,0)
for i in range(5):
    row_of_matrix = [int(i) for i in input().split()]

    if 1 in row_of_matrix:
        eye_position = (i, row_of_matrix.index(1))


print(make_beutiful_matrix(eye_position))


