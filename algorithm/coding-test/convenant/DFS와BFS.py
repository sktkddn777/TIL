from collections import deque

N, M, V = map(int, input().split())
graph = {x: [] for x in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in graph:
    graph[k].sort()

res_d = []
visited = [0] * (N+1)
def dfs(v):
    global res_d, visited
    res_d.append(v)
    visited[v] = 1

    for x in graph[v]:
        if visited[x] == 0:
            dfs(x)

res_b = []
def bfs(v):
    queue = deque([v])
    visited = [0] * (N+1)
    visited[v] = 1
    res_b.append(v)

    while queue:
        x = queue.popleft()
        for g in graph[x]:
            if visited[g] == 0:
                visited[g] = 1
                res_b.append(g)
                queue.append(g)


dfs(V)
bfs(V)

print(*res_d)
print(*res_b)