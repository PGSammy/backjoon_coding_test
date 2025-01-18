def min_difference(A, B):
    len_a = len(A)
    len_b = len(B)

    min_diff = float('inf')

    for i in range(len_b - len_a + 1):
        diff = 0

        for j in range(len_a):
            if A[j] != B[i + j]:
                diff += 1
        min_diff = min(min_diff, diff)

    return min_diff

A, B = input().split()

print(min_difference(A, B))