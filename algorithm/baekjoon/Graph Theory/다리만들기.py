from collections import deque
import sys

input = sys.stdin.readline

def find_bridge(map, c, lst):
  count = [[0] * len(map) for _ in range(len(map))]
  queue = deque(lst)
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < len(map) and 0 <= ty < len(map) and map[tx][ty] != c and count[tx][ty] == 0:
        if map[tx][ty] == 0:
          count[tx][ty] = count[x][y] + 1
          queue.append((tx, ty))
        elif isinstance(map[tx][ty], str):
          return count[x][y]
  return 0

def certify_island(map, i, j, c):
  begin_island_node = [(i, j)]
  queue = deque([(i, j)])
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  while queue:
    x, y = queue.popleft()
    map[x][y] = c
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < len(map) and 0 <= ty < len(map) and map[tx][ty] == 1:
        map[tx][ty] = c
        queue.append((tx, ty))
        begin_island_node.append((tx, ty))
  
  return begin_island_node


N = int(input())
arr = []
island = {}

for _ in range(N):
  arr.append(list(map(int, input().split())))

island_num = 1
for i in range(len(arr)):
  for j in range(len(arr)):
    if arr[i][j] == 1:
      island[chr(island_num)] = certify_island(arr, i, j, chr(island_num))
      island_num += 1

res = []
for k, v in island.items():
  res.append(find_bridge(arr, k, v))

print(min(res))