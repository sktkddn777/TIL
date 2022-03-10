from collections import defaultdict, deque

def bfs(network, visited):
  queue = deque([1])

  while queue:
    num = queue.popleft()
    tmp_lst = network[num]
    for t in tmp_lst:
      if visited[t] == 0:
        queue.append(t)
        visited[t] = 1
  

comNum = int(input())
lineNum = int(input())

visited = [0] * (comNum + 1)
visited[1] = 1
network = defaultdict(list)
for _ in range(lineNum):
  a, b = map(int, input().split())
  network[a].append(b)
  network[b].append(a)

bfs(network, visited)
print(visited.count(1) - 1)