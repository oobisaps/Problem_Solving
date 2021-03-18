string = input()
n = int(input())

def repeatedString(s, n):

    a_count = s.count('a')
    additional_digits = n - len(s)

    a_count += a_count * (additional_digits // len(s)) + s[:(additional_digits % len(s))].count('a')
    
    return a_count

print(repeatedString(string,n))