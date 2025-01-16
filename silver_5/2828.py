import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

left = 1
right = M
total_distance = 0

for _ in range(J):
    apple_pos = int(input())

    if left <= apple_pos <= right:
        continue

    if apple_pos < left:
        move = left - apple_pos
        left = apple_pos
        right = apple_pos + M - 1
        total_distance += move

    if apple_pos > right:
        move = apple_pos - right
        right = apple_pos
        left = apple_pos - M + 1
        total_distance += move

print(total_distance)