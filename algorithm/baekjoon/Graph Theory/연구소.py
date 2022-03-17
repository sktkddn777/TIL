from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

input = sys.stdin.readline

def bfs(tmp_zido, virus):
  queue = deque([virus])

  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  while queue:
    tmp = queue.popleft()
    x, y = tmp[0], tmp[1]
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < N and 0 <= ty < M:
        if tmp_zido[tx][ty] == 0:
          tmp_zido[tx][ty] = 2
          queue.append([tx, ty])

def check_safe(tmp_zido, N):
  ans = 0
  for i in range(N):
    ans += tmp_zido[i].count(0)
  return (ans)
  
N, M = map(int, input().split())
zido = []
for _ in range(N):
  zido.append(list(map(int, input().split())))

comb_lst = combinations([i for i in range(N * M)], 3)
virus = []
for i in range(N):
  for j in range(M):
    if zido[i][j] == 2:
      virus.append([i, j])

max_safe = 0
for comb in list(comb_lst):
  flg = 1
  tmp_zido = deepcopy(zido)
  for i in range(3):
    if tmp_zido[comb[i] // M][comb[i] % M] == 0:
      tmp_zido[comb[i] // M][comb[i] % M] = 1
    else:
      flg = 0
  if flg:
    for v in virus:
      bfs(tmp_zido, v)
    tmp_safe = check_safe(tmp_zido, N)
    if tmp_safe > max_safe:
      max_safe = tmp_safe

print(max_safe)

