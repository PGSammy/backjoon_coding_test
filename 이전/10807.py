n = int(input())

v_list = list(map(int, input().split()))

v = int(input())

count = 0

for i in v_list:
    if i == v:
        count += 1

print(count)