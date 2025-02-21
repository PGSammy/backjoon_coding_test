import sys
input = sys.stdin.readline

# 이분 탐색 (binary search)
def find_start(locations, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if locations[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find_end(locations, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if locations[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

N, M = map(int, input().split())

locations = list(map(int, input().split()))

lines = [list(map(int, input().split())) for _ in range(M)]

locations.sort()

for line in lines:
    start, end = line
    start_idx = find_start(locations, start)
    end_idx = find_end(locations, end)

    print(end_idx - start_idx)