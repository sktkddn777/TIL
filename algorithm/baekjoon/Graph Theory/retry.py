import sys

input = sys.stdin.readline
R, C = map(int, input().split())
board = []
alp = [0] * 26

for _ in range(R):
  board.append(list(map(lambda x : ord(x) - 65, input()[:C])))

alp[board[0][0]] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

def solution(x, y, num):
  global ans
  if ans < num:
    ans = num
  for i in range(4):
    tx = x + dx[i]
    ty = y + dy[i]
    if 0 <= tx < R and 0 <= ty < C and alp[board[tx][ty]] == 0:
      alp[board[tx][ty]] = 1
      solution(tx, ty, num + 1)
      alp[board[tx][ty]] = 0

solution(0, 0, 1)
print(ans)