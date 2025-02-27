import sys
input = sys.stdin.readline

def make_palindrome(name):
    char_count = {}
    for char in name:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_chars = []
    for char, count in char_count.items():
        if count % 2 == 1:
            odd_chars.append(char)

    if len(odd_chars) > 1:
        return "I'm Sorry Hansoo"
    
    result = ""
    middle = ""

    if odd_chars:
        middle = odd_chars[0]
        char_count[middle] -= 1

    for char in sorted(char_count.keys()):
        result += char * (char_count[char] // 2)

    return result + middle + result[::-1]

name = input().strip()

print(make_palindrome(name))