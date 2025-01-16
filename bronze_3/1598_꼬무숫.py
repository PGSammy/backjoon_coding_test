def get_position(num):
    row = (num - 1) // 4
    col = (num - 1) % 4

    return row, col

n1, n2 = map(int, input().split())

row1, col1 = get_position(n1)
row2, col2 = get_position(n2)

distance = abs(row1 - row2) + abs(col1 - col2)

print(distance)