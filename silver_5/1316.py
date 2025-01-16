def is_group_word(word):
    seen = set()
    prev_char = None

    for char in word:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True

N = int(input())
words = [input() for _ in range(N)]
result = sum(1 for word in words if is_group_word(word))
print(result)