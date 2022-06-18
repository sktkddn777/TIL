import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치
for i in range(R):
  if board[i][0] == -1:
    up = i
    down = i+1
    break

# 위쪽 청소
def AirCleanUp():
  up_dx = [0, -1, 0, 1]
  up_dy = [1, 0, -1, 0]

  tmp_value = 0
  direct = 0
  x, y = up, 1
  while True:
    if x == up and y == 0:
      break
    tx = x + up_dx[direct]
    ty = y + up_dy[direct]
    if 0 <= tx < R and 0 <= ty < C:
      board[x][y], tmp_value = tmp_value, board[x][y]
      x, y = tx, ty
    else:
      direct += 1

# 아래쪽 청소
def AirCleanDown():
  down_dx = [0, 1, 0, -1]
  down_dy = [1, 0, -1, 0]

  tmp_value = 0
  direct = 0
  x, y = down, 1
  while True:
    if x == down and y == 0:
      break
    tx = x + down_dx[direct]
    ty = y + down_dy[direct]
    if 0 <= tx < R and 0 <= ty < C:
      board[x][y], tmp_value = tmp_value, board[x][y]
      x, y = tx, ty
    else:
      direct += 1


# 미세 먼제 확산
def SpreadMise():
  global board
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  tmp_board = [[0] * C for _ in range(R)]
  for x in range(R):
    for y in range(C):
      if board[x][y] > 0:
        cnt = 0
        for i in range(4):
          tx = x + dx[i]
          ty = y + dy[i]
          if 0 <= tx < R and 0 <= ty < C and board[tx][ty] != -1:
            tmp_board[tx][ty] += board[x][y] // 5 # 확산된 곳 미세먼지 추가
            cnt += 1
        board[x][y] -= (board[x][y] // 5) * cnt # 기존 미세먼지 감소

  for i in range(R):
    for j in range(C):
      board[i][j] += tmp_board[i][j]

def main():
  for _ in range(T):
    SpreadMise()
    AirCleanUp()
    AirCleanDown()
  
  ans = 0
  for i in range(R):
    for j in range(C):
      if board[i][j] > 0:
        ans += board[i][j]
  print(ans)
main()


