import sys
input = sys.stdin.readline

gear1 = input().strip()
gear2 = input().strip()

if len(gear1) > len(gear2):
    gear1, gear2 = gear2, gear1

max_overlap = 0

for k in range(len(gear1)):
    can_mesh = True
    for i in range(k+1):
        if gear1[-k+i-1] == '2' and gear2[i] == '2':
            can_mesh = False
            break
    if can_mesh:
        max_overlap = max(max_overlap, k+1)

for k in range(len(gear1)):
    can_mesh = True
    for i in range(k+1):
        if gear1[i] == '2' and gear2[-k+i-1] == '2':
            can_mesh = False
            break
    if can_mesh:
        max_overlap = max(max_overlap, k+1)

for k in range(len(gear2) - len(gear1) + 1):
    can_mesh = True
    for i in range(len(gear1)):
        if gear1[i] == '2' and gear2[i+k] == '2': 
            can_mesh = False
            break
    if can_mesh:
        max_overlap = max(max_overlap, len(gear1))
        break

print(len(gear1) + len(gear2) - max_overlap)