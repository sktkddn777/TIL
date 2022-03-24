import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  zido = []
  for _ in range(h):
    zido.append(list(map(int, input().split())))

  def dfs(x, y):
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    zido[x][y] = 0
    for i in range(8):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < h and 0 <= ty < w:
        if zido[tx][ty] == 1:
          dfs(tx, ty)

  ans = 0
  for i in range(h):
    for j in range(w):
      if zido[i][j] == 1:
        dfs(i, j)
        ans += 1

  print(ans)