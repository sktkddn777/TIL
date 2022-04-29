from collections import deque

N, K = map(int, input().split())
visited = [float('inf')] * (100001)

def bfs():
    res = []
    queue = deque([(N, 0)])
    while queue:
        x, c = queue.popleft()
        if x == K:
            res.append(c)
        else:
            if x-1 >= 0 and c <= visited[x-1]:
                visited[x-1] = c
                queue.append((x-1, c+1))
            if x+1 <= K and c <= visited[x+1]:
                visited[x+1] = c
                queue.append((x+1, c+1))
            if 2*x < 100001 and 2*x < 2*K and c <= visited[2*x]:
                visited[2*x] = c
                queue.append((2*x, c+1))
    return res

res = bfs()
print(res[0])
print(len(res))