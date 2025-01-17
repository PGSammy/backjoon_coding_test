L = int(input())
nums = list(map(int, input().split()))
n = int(input())

nums.append(0)
nums.sort()

for i in range(len(nums) - 1):
    if nums[i] == n or nums[i + 1] == n:
        print(0)
        exit()
    if nums[i] < n < nums[i + 1]:
        result = (n - nums[i]) * (nums[i + 1] - n) - 1
        print(result)
        exit()

print(0)