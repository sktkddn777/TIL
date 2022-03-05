from collections import deque

def bfs(miro, N, M):
  root = [(0, 0)]
  queue = deque(root)
  visited = [[0] * M for _ in range(N)]
  visited[0][0] = 1
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  while queue:
    tmp = queue.popleft()
    x, y = tmp[0], tmp[1]
 
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < N and 0 <= ty < M:
        if miro[tx][ty] == 1 and visited[tx][ty] == 0:
          visited[tx][ty] = visited[x][y] + 1
          queue.append((tx, ty))

  print(visited[N-1][M-1])

N, M = map(int, input().split())
miro = []
for _ in range(N):
  miro.append(list(map(int, input())))

bfs(miro, N, M)
