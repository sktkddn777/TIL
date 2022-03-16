
# def get_next(x_lst, visited):
#   tmp = []
#   for x in x_lst:
#     if 0 <= x+1 <= 100000:
#       if visited[x+1] == 0:
#         tmp.append(x+1)
#     if 0 <= x-1 <= 100000:
#       if visited[x-1] == 0 :
#         tmp.append(x-1)
#     if 0 <= 2*x <= 100000:
#       if visited[2*x] == 0:
#         tmp.append(2*x)
#   return list(set(tmp))

# N, K = map(int, input().split())
# visited = [0] * (100001)
# ans = 0
# if N != K:
#   num_lst = [N]
#   while visited[K] == 0:
#     tmp = get_next(num_lst, visited)
#     for n in tmp:
#       visited[n] = ans + 1
#     num_lst = tmp
#     ans += 1
# print(ans)

from collections import deque

def bfs(n, k, visited):
  queue = deque([n])
  
  while queue:
    x = queue.popleft()
    if x == k:
      print(visited[x])
      break
    for y in (x+1, x-1, 2*x):
      if 0 <= y <= 100000:
        if visited[y] == 0:
          visited[y] = visited[x] + 1
          queue.append(y)

N, K = map(int, input().split())
visited = [0] * (100001)

bfs(N, K, visited)