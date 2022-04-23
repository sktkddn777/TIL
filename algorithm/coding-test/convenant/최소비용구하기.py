import heapq, sys

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = {x:[] for x in range(1, N+1)}
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
distance = [float('inf')] * (N+1)
queue = [(0, start)]
distance[start]=0

while queue:
    dis, now = heapq.heappop(queue)
    if dis > distance[now]:
        continue
    for g in graph[now]:
        cost = dis + g[1]
        if cost < distance[g[0]]:
            distance[g[0]] = cost
            heapq.heappush(queue, (cost, g[0]))

print(distance[end])