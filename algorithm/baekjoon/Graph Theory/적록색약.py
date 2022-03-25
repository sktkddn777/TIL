import sys
import copy
sys.setrecursionlimit(10 ** 6)

def dfs(node, color, arr, k):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  arr[node[0]][node[1]] = 'X'
  for i in range(4):
    tx = node[0] + dx[i]
    ty = node[1] + dy[i]
    if 0 <= tx < len(arr) and 0 <= ty < len(arr):
      if arr[tx][ty] == color:
        dfs((tx, ty), color, arr, k)
      else:
        if k % 2 == 1 and color == 'R':
          if arr[tx][ty] == 'G':
            dfs((tx, ty), color, arr, k)
        elif k % 2 == 1 and color == 'G':
          if arr[tx][ty] == 'R':
            dfs((tx, ty), color, arr, k)

N = int(input())
arr = []
for _ in range(N):
  arr.append(list(input()))

for k in range(2):
  ans = 0
  tmp_arr = copy.deepcopy(arr)
  for i in range(N):
    for j in range(N):
      if tmp_arr[i][j] in ['R', 'G', 'B']:
        dfs((i, j), tmp_arr[i][j], tmp_arr, k)
        ans += 1
  print(ans, end=' ')