def find_fraction(X):
    diagonal = 1
    while X > diagonal:
        X -= diagonal
        diagonal += 1

    if diagonal % 2 == 1:
        numerator = diagonal - (X - 1)
        denominator = X
    else:
        numerator = X
        denominator = diagonal - (X - 1)

    return numerator, denominator

X = int(input())

numerator, denominator = find_fraction(X)

print(f"{numerator}/{denominator}")