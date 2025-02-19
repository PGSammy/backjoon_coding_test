S = int(input())

i = 0
cnt = 0
while True:
    if S > i:
        i += 1
        S = S-i
        cnt += 1
    else:
        print(cnt)
        break