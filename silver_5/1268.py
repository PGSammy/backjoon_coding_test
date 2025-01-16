n = int(input())
students = [[0 for _ in range(5)] for _ in range(n)]

for i in range(n):
    students[i] = list(map(int, input().split()))

def count_same_class():
    max_cnt = -1
    leader = 0

    for i in range(n):
        cnt = 0
        checked = set()

        for grade in range(5):
            for j in range(n):
                if i == j or j in checked:
                    continue

                if students[i][grade] == students[j][grade]:
                    cnt += 1
                    checked.add(j)

        if cnt > max_cnt:
            max_cnt = cnt
            leader = i + 1

    return leader

print(count_same_class())