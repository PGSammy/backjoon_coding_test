import sys
input = sys.stdin.readline

heights = []

for _ in range(9):
    heights.append(int(input()))

total = sum(heights)

found = False
for i in range(8):
    for j in range(i+1, 9):
        if total - heights[i] - heights[j] == 100:
            real_dwarfs = [heights[k] for k in range(9) if k != i and k != j]
            found = True
            break
    if found:
        break

real_dwarfs.sort()
for height in real_dwarfs:
    print(height)