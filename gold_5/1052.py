def min_bottles_to_buy(N, K):
    def count_set_bits(x):
        return bin(x).count('1')
    
    bottles_to_buy = 0

    while count_set_bits(N) > K:
        N += 1
        bottles_to_buy += 1

    return bottles_to_buy

N, K = map(int, input().split())

result = min_bottles_to_buy(N, K)

print(result)