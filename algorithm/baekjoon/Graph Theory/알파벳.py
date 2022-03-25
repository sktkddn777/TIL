import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(coor, alp_lst, arr, count):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  for i in range(4):
    tx = coor[0] + dx[i]
    ty = coor[1] + dy[i]
    if 0 <= tx < len(arr) and 0 <= ty < len(arr[0]):
      if arr[tx][ty] not in alp_lst:
        count[tx][ty] = max(count[tx][ty], count[coor[0]][coor[1]] + 1)
        dfs((tx, ty), alp_lst + [arr[tx][ty]], arr, count)

R, C = map(int, input().split())
arr = []
count = [[0] * C for _ in range(R)]
for _ in range(R):
  arr.append(list(input()))
count[0][0] = 1
dfs((0, 0), [arr[0][0]], arr, count)

print(count)