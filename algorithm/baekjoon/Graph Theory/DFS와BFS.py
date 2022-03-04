from collections import deque

def dfs(node, start, visited = []):
  visited.append(start)
  for x in node[start]:
    if x not in visited:
      dfs(node, x, visited)
  return visited

def bfs(node, root):
  queue = deque([root])
  visited = [root]

  while queue:
    num = queue.popleft()
    for n in node[num]:
      if n not in visited:
        visited.append(n)
        queue.append(n)
  return visited

N, M, V = map(int, input().split())
node = [[] for _ in range(N + 1)]

for _ in range(M):
  start, end = map(int, input().split())
  node[start].append(end)
  node[end].append(start)

for i in range(1, N + 1):
  node[i] = sorted(node[i])

for x in dfs(node, V):
  print(x, end =' ')
print()
for x in bfs(node, V):
  print(x, end =' ')