import sys
input = sys.stdin.readline
cnt = 0

N = int(input())
queen_lst = [0] * N

def is_promise(x):
  for i in range(x):
    if queen_lst[i] == queen_lst[x] or abs(queen_lst[i] - queen_lst[x]) == abs(i - x):
      return 0
  return 1

def queen(x):
  global cnt
  if x == N:
    cnt += 1
    return 
  for i in range(N):
    queen_lst[x] = i
    if is_promise(x):
      queen(x+1)
    
queen(0)
print(cnt)