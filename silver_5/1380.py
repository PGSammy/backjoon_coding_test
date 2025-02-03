def find_missing_earring():
    scenario = 1
    while True:
        n = int(input())
        if n == 0:
            break

        names = []
        for _ in range(n):
            names.append(input())

        count = {}

        for _ in range(2*n - 1):
            num, _ = input().split()
            num = int(num)
            count[num] = count.get(num, 0) + 1

        for student_num, appear_count in count.items():
            if appear_count == 1:
                print(f"{scenario} {names[student_num - 1]}")
                break

        scenario += 1

find_missing_earring()