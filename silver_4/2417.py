n = int(input())

def find_sqrt(n):
    if n == 0:
        return 0
    
    left = 1
    right = n

    while right > left + 1:
        mid = (left + right) // 2

        if mid > n // mid:
            right = mid
        else:
            left = mid

    if left * left >= n:
        return left
    else:
        return right
    
print(find_sqrt(n))