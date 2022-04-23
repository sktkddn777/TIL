import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = {x:[] for x in range(1, V+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [0] * (V+1)
queue = [(0, 1)]
cnt = 0
ans = 0

while queue:
    if cnt == V:
        break
    c, now = heapq.heappop(queue)
    if not visited[now]:
        visited[now] = 1
        cnt += 1
        ans += c
        for g in graph[now]:
            heapq.heappush(queue, g)

print(ans)