from collections import deque

def bfs(N, n1, n2, zido, visited):
  queue = deque([(n1, n2)])
  visited[n1][n2] = 1
  res = 1
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  while queue:
    tmp = queue.popleft()
    x, y = tmp[0], tmp[1]
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < N and 0 <= ty < N:
        if zido[tx][ty] == 1 and visited[tx][ty] == 0:
          visited[tx][ty] = 1
          queue.append((tx, ty))
          res += 1

  return res

N = int(input())

zido = []
visited = [[0] * N for _ in range(N)]
for _ in range(N):
  zido.append(list(map(int, input())))

ans = []
for x in range(N):
  for y in range(N):
    if zido[x][y] == 1 and visited[x][y] == 0:
      ans.append(bfs(N, x, y, zido, visited))

ans.sort()
print(len(ans))
for x in ans: print(x)

