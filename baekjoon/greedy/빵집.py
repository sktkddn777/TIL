from collections import deque

R, C = map(int, input().split())
map_lst = []
for _ in range(R):
  map_lst.append(list(input()))

dx = [0, -1, 1]
dy = [1, 1, 1]

for i in range(R):
  queue = deque([i,0])

  while queue:
    