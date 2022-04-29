from collections import deque
N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0

def bfs():
    queue = deque([(N, 0)])

    while queue:
        x, c = queue.popleft()
        if x == K:
            return c
            
        if 2*x < 100001 and (visited[2*x] == -1 or c < visited[2*x]):
            visited[2*x] = c
            queue.append((2*x, c))
        if x-1 >= 0 and (visited[x-1] == -1 or c < visited[x-1]):
            visited[x-1] = c
            queue.append((x-1, c+1))
        if x+1 < 100001 and (visited[x+1] == -1 or c < visited[x+1]):
            visited[x+1] = c
            queue.append((x+1, c+1))
        
print(bfs())