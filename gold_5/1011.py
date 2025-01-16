def calculate_min_moves(x, y):
    distance = y - x
    move = 0
    max_distance = 0

    while max_distance < distance:
        move += 1
        max_distance += (move + 1) // 2

    return move

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    result = calculate_min_moves(x, y)

    print(result)