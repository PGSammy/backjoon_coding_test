while True:
    N = input()

    if N == "0":
        break

    total_len = 2 + len(N) - 1

    for i in N:
        if i == '1':
            total_len += 2
        elif i == '0':
            total_len += 4
        else:
            total_len += 3

    print(total_len)
