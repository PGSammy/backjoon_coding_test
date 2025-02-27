import sys
input = sys.stdin.readline

n = int(input())
moves = input()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
dir = 0

visited = set([(x, y)])

for move in moves:
    if move == 'F':
        x += dx[dir]
        y += dy[dir]
        visited.add((x, y))
    elif move == 'L':
        dir = (dir + 1) % 4
    elif move == 'R':
        dir = (dir - 1) % 4

min_x = min(x for x, y in visited)
max_x = max(x for x, y in visited)
min_y = min(y for x, y in visited)
max_y = max(y for x, y in visited)

for i in range(min_x, max_x + 1):
    row = ""
    for j in range(min_y, max_y + 1):
        if (i, j) in visited:
            row += "."
        else:
            row += "#"

    print(row)