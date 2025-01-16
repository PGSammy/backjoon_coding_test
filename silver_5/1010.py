# 조합 (Combination) 구할 때 사용하는 것
# math를 활용하여 comb를 하면 조합 공식을 사용할 수 있음
import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    answer = math.comb(m, n)
    print(answer)

'''
def combination(n, r):
    numerator = 1
    denominator = 1

    for i in range(r):
        numerator *= (n - 1)
        denominator *= (i + 1)

    return numerator // denominator

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    answer = combination(m, n)
    print(answer)
'''