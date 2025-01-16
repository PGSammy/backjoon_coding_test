N, M = map(int, input().split())

grid = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            grid[i][j] += 1

invisible = sum(1 for i in range(100) for j in range(100) if grid[i][j] > M)

print(invisible)