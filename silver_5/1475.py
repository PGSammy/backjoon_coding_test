N = input()
ans = [0] * 10

for i in range(len(N)):
    num = int(N[i])

    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1

print(max(ans))