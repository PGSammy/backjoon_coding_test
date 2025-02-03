def binary_serach(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

result = []
for target in targets:
    result.append(binary_serach(cards, target))
print(*result)