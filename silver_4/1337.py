import sys
import bisect # 이분 탐색 라이브러리
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
min_add = 5

for i in range(N):
    start = num_list[i]
    end = start + 4

    pos = bisect.bisect_right(num_list, end)

    count = pos - i

    min_add = min(min_add, 5 - count)

print(min_add)