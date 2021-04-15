def rotLeft(a, d):
    for i in range(d):
        a.append(a[0])
        a.pop(0)
    
    return a


def array_left_rotation(a, n, k):
    return a[k:] + a[:k]