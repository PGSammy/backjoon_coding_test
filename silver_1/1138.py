N = int(input())
people = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    current = i + 1
    bigger = people[i]

    empty = 0
    pos = 0
    while empty < bigger:
        if result[pos] == 0:
            empty += 1
        pos += 1

    while result[pos] != 0:
        pos += 1
    result[pos] = current

print(*result)