A, B, N = map(int, input().split())

def find_nth_decimal(A, B, N):
    A = A % B
    for _ in range(N - 1):
        A = (A * 10) % B
    return (A * 10) // B

print(find_nth_decimal(A, B, N))