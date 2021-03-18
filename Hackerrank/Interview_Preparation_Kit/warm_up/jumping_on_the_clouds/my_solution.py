from functools import reduce


n = input()

clouds = [int(c) for c in input().split()]


def jumpingOnClouds(clouds,n):

    def get_indexes(clouds, el):
        indexes = []

        for i in range(len(clouds)):
            if clouds[i] == el:
                indexes.append(i+1)
        
        return [0] + indexes + [n-1]

    min_count = 0
    
    thunderheads  = get_indexes(clouds, 1)


    for i in range(len(thunderheads) - 1):
        distance = thunderheads[i+1] - thunderheads[i]

        if distance % 2 != 0:
            min_count += 1 + (distance - 1) // 2
        else:
            min_count += distance // 2
    
    return min_count

print(jumpingOnClouds(clouds,n))

