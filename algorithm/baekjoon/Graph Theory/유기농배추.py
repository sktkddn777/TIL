from collections import deque

T = int(input())
for _ in range(T):
  ans = 0
  M, N, K = map(int, input().split())
  visited = [[0] * M for _ in range(N)]
  baechu = [[0] * M for _ in range(N)]
  for _ in range(K):
    X, Y = map(int, input().split())
    baechu[Y][X] = 1
  
  def bfs(i, j, baechu, visited):
    queue = deque([(i, j)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
      tmp = queue.popleft()
      x, y = tmp[0], tmp[1]
      for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < M:
          if visited[tx][ty] == 0 and baechu[tx][ty] == 1:
            visited[tx][ty] = 1
            queue.append((tx, ty))
  
  for i in range(N):
    for j in range(M):
      if baechu[i][j] == 1 and visited[i][j] == 0:  
        bfs(i, j, baechu, visited)
        ans += 1
      
  print(ans)