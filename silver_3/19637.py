import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
titles = []

for _ in range(N):
    name, power = input().split()
    titles.append((int(power), name))

def binary_search(power):
    left, right = 0, len(titles) - 1

    while left <= right:
        mid = (left + right) // 2
        if titles[mid][0] >= power:
            right = mid - 1
        else:
            left = mid + 1
    return titles[left][1]

for _ in range(M):
    power = int(input())
    print(binary_search(power))