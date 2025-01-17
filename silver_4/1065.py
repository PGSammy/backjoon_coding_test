def hansu(n):
    if n < 100:
        return n
    
    count = 99

    for i in range(100, n + 1):
        num = str(i)

        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            count += 1

    return count

n = int(input())
result = hansu(n)

print(result)