N, M = map(int, input().split())

package = []
one_price = []

for _ in range(M):
    A, B = map(int, input().split())
    package.append(A)
    one_price.append(B)

package_num = N // 6
one_num = N % 6

min_package = min(package)
min_one = min(one_price)

if min_one * 6 <= min_package:
    result = min_one * N
else:
    result = min((N//6) * min_package + (N%6) * min_one,  
                 ((N//6) + 1) * min_package,             
                 N * min_one)                             

print(result)