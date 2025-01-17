def win(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1
    
n, a, b = map(int, input().split())
round = 1

while a != 0 and b != 0:
    if abs(a - b) == 1 and (a // 2 != b // 2):
        break
    a = win(a)
    b = win(b)
    round += 1

    if a == b:
        rount = -1
        break

print(round)