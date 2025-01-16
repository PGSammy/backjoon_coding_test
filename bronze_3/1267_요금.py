N = int(input())

num_call = list(map(int, input().split()))

sum_A = 0
sum_B = 0

for i in num_call:
    result_A = (i // 30) + 1
    result_B = (i // 60) + 1

    sum_A += result_A * 10
    sum_B += result_B * 15

if sum_A < sum_B:
    print(f"Y {sum_A}")
elif sum_A > sum_B:
    print(f"M {sum_B}")
else:
    print(f"Y M {sum_A}")
