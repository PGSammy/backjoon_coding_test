import sys
input = sys.stdin.readline

def find_largest_square():
    global N, M, grid, min_val

    for k in range(min_val, 0, -1):
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                if grid[i][j] == grid[i][j+k-1] == grid[i+k-1][j] == grid[i+k-1][j+k-1]:
                    return k * k
                
    return 1

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

min_val = min(N, M)

print(find_largest_square())