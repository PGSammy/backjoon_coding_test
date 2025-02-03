N, M = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M, K = map(int, input().split())

B = []
for _ in range(M):
    row = list(map(int, input().split()))
    B.append(row)

result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(*row)