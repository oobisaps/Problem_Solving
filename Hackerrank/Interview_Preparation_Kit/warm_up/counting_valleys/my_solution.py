n = int(input())
steps = input()

def countingValleys(n, s):
    sea_level, count = (0,0)

    for step in s:
        if step == 'U':

            if sea_level == -1:
                count += 1

            sea_level += 1
        
        else:
            sea_level -= 1
        

    return count


print(countingValleys(n, steps))


