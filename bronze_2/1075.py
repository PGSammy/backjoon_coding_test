def find_last_two_digits(N, F):
    base = (N // 100) * 100

    for i in range(100):
        if (base + i) % F == 0:
            return f"{i:02}"
        
N = int(input())
F = int(input())

result = find_last_two_digits(N, F)

print(result)