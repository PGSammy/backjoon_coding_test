X = int(input())
stick_len = 64
count = 0

while X > 0:
    if stick_len > X:
        stick_len //= 2
    else:
        count += 1
        X -= stick_len

print(count)