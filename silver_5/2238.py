# import sys
# input = sys.stdin.readline

# D = {}
# U, N = map(int, input().split())

# for _ in range(N):
#     S, P = input().split()
#     P = int(P)

#     if P <= U:
#         if P in D:
#             D[P] += [S]
#         else:
#             D[P] = [S]

# min_name = min([len(j) for j in D.values()])
# min_won = min([j for j in D.keys() if len(D[j]) == min_name])

# print(D[min_won][0], min_won)

from collections import defaultdict

U, N = map(int, input().split())
price_count = defaultdict(int)
price_first_bidder = {}

for i in range(N):
    S, P = input().split()
    P = int(P)

    price_count[P] += 1

    if P not in price_first_bidder:
        price_first_bidder[P] = (S, P)

min_count = min(price_count.values())
rare_prices = [price for price, count in price_count.items() if count == min_count]

lowest_rare_prices = min(rare_prices)

winner_name, winner_price = price_first_bidder[lowest_rare_prices]

print(winner_name, winner_price)