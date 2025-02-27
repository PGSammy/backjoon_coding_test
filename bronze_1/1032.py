import sys
input = sys.stdin.readline

n = int(input())

files = []

for _ in range(n):
    files.append(input())

result = list(files[0])

for i in range(len(result)):
    for j in range(1, n):
        if files[j][i] != result[i]:
            result[i] = '?'
            break

print(''.join(result))