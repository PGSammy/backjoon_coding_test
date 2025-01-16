for _ in range(3):
    N = int(input())

    list_N = []

    for i in range(N):
        num = int(input())

        list_N.append(num)

    total = 0

    for j in list_N:
        total += j

    if total == 0:
        print("0")
    elif total > 0:
        print("+")
    else:
        print("-")