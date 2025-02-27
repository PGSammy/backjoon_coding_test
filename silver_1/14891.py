import sys
from collections import deque
input = sys.stdin.readline

wheels = []
deq = deque()

for _ in range(4):
    wheel = deque(map(int, input().strip()))
    wheels.append(wheel)

K = int(input()) # 회전 횟수

for _ in range(K):
    num, direction = map(int, input().split())
    num -= 1

    to_rotate = [0] * 4
    to_rotate[num] = direction

    # 왼쪽 톱니 확인
    for i in range(num, 3):
        if wheels[i][2] != wheels[i+1][6]:
            to_rotate[i+1] = -to_rotate[i]
        else:
            break

    # 오른쪽 톱니 확인
    for i in range(num, 0, -1):
        if wheels[i][6] != wheels[i-1][2]:
            to_rotate[i-1] = -to_rotate[i]
        else:
            break

    # 회전시키기
    for i in range(4):
        if to_rotate[i] != 0:
            wheels[i].rotate(to_rotate[i])

score = 0
for i in range(4):
    if wheels[i][0] == 1:
        score += 2**i

print(score)