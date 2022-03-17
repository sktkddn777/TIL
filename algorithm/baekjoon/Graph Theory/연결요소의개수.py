from collections import defaultdict, deque
import sys

input = sys.stdin.readline
def bfs(x, node, visited):
  queue = deque([x])
  visited[x] = 1
  while queue:
    d = queue.popleft()
    for n in node[d]:
      if visited[n] == 0:
        visited[n] = 1
        queue.append(n)

N, M = map(int, input().split())
node = defaultdict(list)
visited = [0] * (N+1)
for _ in range(M):
  u, v = map(int, input().split())
  node[u].append(v)
  node[v].append(u)

ans = 0
for i in range(1, N+1):
  if visited[i] == 0:
    bfs(i, node, visited)
    ans += 1
print(ans)