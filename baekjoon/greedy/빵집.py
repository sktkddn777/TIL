'''
dfs를 통해 방문 방법을 탐색한다.

처음에 생각을 잘못해 정답 코드를 참고하였다.
'''

R, C = map(int, input().split())
map_lst = []
for _ in range(R):
  map_lst.append(list(input()))

visited = [[0] * C for _ in range(R)]

dx = [-1, 0, 1]

def dfs(x, y):
  if y == C-1:
    return True
  
  for i in range(3):
    tx = x + dx[i]
    if 0<= tx < R:
      if visited[tx][y+1] == 0 and map_lst[tx][y+1] == '.':
        visited[tx][y+1] = 1
        if dfs(tx, y+1):
          return True
  return False

total = 0
for x in range(R):
  if dfs(x, 0):
    total += 1

print(total)