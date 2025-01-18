def get_rank(n, new_score, p, scores):
    if n == 0:
        return 1
    
    if n == p and new_score <= scores[-1]:
        return -1
    
    if n == p:
        scores.pop()
    
    scores.append(new_score)
    scores = sorted(scores, reverse=True)

    rank = 1
    for i in range(len(scores)):
        if scores[i] == new_score:
            return rank
        rank += 1

n, new_score, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

answer = get_rank(n, new_score, p, scores)

print(answer)