# https://codeforces.com/problemset/problem/71/A

def too_long_word(word):
    if len(word) <= 10:
        return word
    
    return word[0] + str(len(word) - 2) + word[-1]

n = int(input())
words = []

for _ in range(n):
    words.append(input())

for word in words:
    print(too_long_word(word))