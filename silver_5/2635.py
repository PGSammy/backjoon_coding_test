def make_sequence(first, second):
    sequence = [first, second]
    while True:
        next_num = sequence[-2] - sequence[-1]
        if next_num < 0:
            break
        sequence.append(next_num)
    return sequence

def solve(n):
    max_length = 0
    max_sequence = []

    for second in range(1, n + 1):
        sequence = make_sequence(n ,second)
        if len(sequence) > max_length:
            max_length = len(sequence)
            max_sequence = sequence

    return max_length, max_sequence

n = int(input())

length, sequence = solve(n)

print(length)
print(' '.join(map(str, sequence)))