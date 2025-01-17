N = int(input())
A = list(map(int, input().split()))

pair = [(A[i], i) for i in range(N)]

pair.sort()

p = [0] * N
for i in range(N):
    p[pair[i][1]] = i

print(*p)