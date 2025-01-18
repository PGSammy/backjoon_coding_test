def find_min_digits(n, numbers):
    length = len(numbers[0])

    for k in range(1, length + 1):
        number_set = set()
        for num in numbers:
            number_set.add(num[-k:])

        if len(number_set) == n:
            return k
        
    return length

n = int(input())
numbers = [input() for _ in range(n)]
print(find_min_digits(n, numbers))