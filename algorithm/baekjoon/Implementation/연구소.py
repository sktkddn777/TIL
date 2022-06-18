from collections import deque
import sys
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def virus(tmp_board, virus_loc):
  queue = deque([virus_loc])
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < N and 0 <= ty < N:
        if tmp_board[tx][ty] == 0:
          tmp_board[tx][ty] = 2
          queue.append([tx, ty])

def dfs(cnt):
  global result

  if cnt == 3:
    tmp_board = deepcopy(board)
    virus_loc = []
    for i in range(N):
      for j in range(M):
        if tmp_board[i][j] == 2:
          virus_loc.append([i, j])
    
    virus(tmp_board, virus_loc)
    safe_area = 0
    for i in range(N):
      for j in range(M):
        if tmp_board[i][j] == 0:
          safe_area += 1
    result = max(result, safe_area)
    return

  for i in range(N):
    for j in range(M):
      if board[i][j] == 0:
        board[i][j] = 1
        dfs(cnt+1)
        board[i][j] = 0

dfs(0)
print(result)