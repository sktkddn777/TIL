from collections import deque

N = int(input())
M = int(input())

graph = {x: [] for x in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    ans = 0
    queue = deque([1])
    visted = [0] * (N+1)
    visted[1] = 1

    while queue:
        x = queue.popleft()
        for g in graph[x]:
            if visted[g] == 0:
                visted[g] = 1
                queue.append(g)
                ans += 1
    return ans

print(bfs())

