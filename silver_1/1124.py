# def is_prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             D[x] = D[x//i] + 1
#             return False
#     D[x] = 1
#     return True

# n, m = map(int, input().split())

# D = [0] * (m + 1)
# res = [False] * (m + 1)
# for i in range(2, m + 1):
#     res[i] = is_prime(i)

# ans = 0
# for i in range(n, m + 1):
#     ans += res[D[i]]
# print(ans)

def get_prime_factors(n):
    count = 0
    d = 2

    while d * d <= n:
        while n % d == 0:
            count += 1
            n //= d
        d += 1
    if n > 1:
        count += 1
    return count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(A, B):
    count = 0
    for i in range(A, B + 1):
        factors_count = get_prime_factors(i)
        if is_prime(factors_count):
            count += 1
    return count

A, B = map(int, input().split())
print(solve(A, B))