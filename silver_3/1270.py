import sys
input = sys.stdin.readline

# 땅의 개수
N = int(input())

# 땅의 개수 만큼 병사 수
for i in range(N):
    soldiers = list(map(int, input().split()))

    num_soldiers = soldiers[0]
    half_soldiers = num_soldiers // 2

    count = {}

    for soldier_id in soldiers[1:]:
        if soldier_id in count:
            count[soldier_id] += 1
        else:
            count[soldier_id] = 1

    dominant_soldier = None

    for soldier_id, freq in count.items():
        if freq > half_soldiers:
            dominant_soldier = soldier_id
            break

    if dominant_soldier:
        print(dominant_soldier)
    else:
        print("SYJKGW")