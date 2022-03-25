import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, arr, N):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  arr[node[0]][node[1]] = 0
  for i in range(4):
    tx = node[0] + dx[i]
    ty = node[1] + dy[i]
    if 0 <= tx < len(arr) and 0 <= ty < len(arr):
      if arr[tx][ty] > N:
        dfs([tx, ty], arr, N)

N = int(input())
arr = []
max_num = 0
for i in range(N):
  arr.append(list(map(int, input().split())))
  if max_num < max(arr[i]):
    max_num = max(arr[i])

ans = []
for k in range(max_num):
  safe = 0
  tmp = copy.deepcopy(arr)
  for i in range(N):
    for j in range(N):
      if tmp[i][j] > k:
        dfs([i, j], tmp, k)
        safe += 1
  ans.append(safe)

print(max(ans))