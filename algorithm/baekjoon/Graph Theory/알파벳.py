import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(lambda x : ord(x) - 65, input())) for _ in range(R)]

ans = 0
alpha = [0] * 26

def dfs(coor, count):
  global ans
  ans = max(ans, count)
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  for i in range(4):
    tx = coor[0] + dx[i]
    ty = coor[1] + dy[i]
    if 0 <= tx < R and 0 <= ty < C and alpha[arr[tx][ty]] == 0:
      alpha[arr[tx][ty]] = 1
      dfs((tx, ty), count + 1)
      alpha[arr[tx][ty]] = 0

alpha[arr[0][0]] = 1
dfs((0, 0), 1)
print(ans)