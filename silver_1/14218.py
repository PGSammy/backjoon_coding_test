from collections import deque

def bfs(graph, n):
    distances = [-1] * (n + 1)
    distances[1] = 0

    q = deque([1])

    while q:   
        current = q.popleft()

        for next_city in graph[current]:
            if distances[next_city] == -1:
                distances[next_city] = distances[current] + 1
                q.append(next_city)

    return distances[1:]

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

p = int(input())

for _ in range(p):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

    distances = bfs(graph, n)
    print(*distances)