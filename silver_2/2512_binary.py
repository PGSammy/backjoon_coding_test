# binary search
import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
M = int(input())

start = 1
end = max(money)

if sum(money) <= M:
    print(max(money))
else:
    result = 0
    while start <= end:
        mid = (start + end) // 2

        total = sum(min(x, mid) for x in money)

        if total <= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)

