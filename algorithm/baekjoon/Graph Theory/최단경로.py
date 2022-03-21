# from collections import deque
# import sys

# input = sys.stdin.readline
# V, E = map(int, input().split())
# root = int(input())
# graph = []
# weight = [float('inf')] * (V + 1)
# visited = [0] * (V + 1)
# weight[root] = 0
# visited[root] = 1

# for _ in range(E):
#   graph.append(list(map(int, input().split())))

# queue = deque([root])
# while queue:
#   n = queue.popleft()
#   for g in graph:
#     if g[0] == n:
#       if visited[g[1]] == 0:
#         queue.append(g[1])
#         weight[g[1]] = min(weight[g[1]], weight[g[0]] + g[2])

# for i in range(1, V + 1):
#   print(weight[i])

import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
root = int(input())
queue = []
graph = [[] for _ in range(V + 1)]
weight = [float('inf')] * (V + 1)
weight[root] = 0

heapq.heappush(queue, (0, root))
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

while queue:
  w, cur = heapq.heappop(queue)
  if w > weight[cur]:
    continue
  for x in graph[cur]:
    cost = x[1] + w
    if cost < weight[x[0]]:
      heapq.heappush(queue, (cost, x[0]))
      weight[x[0]] = cost

for w in range(1, V+1):
  print(weight[w] if weight[w] != float('inf') else "INF")