def last_computer_number(a, b):
    return pow(a, b, 10) or 10

T = int(input())

for i in range(T):
    a, b = map(int, input().split())

    result = last_computer_number(a, b)

    print(result)