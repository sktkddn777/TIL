from collections import deque


N, M, K = map(int, input().split())
lst = [[0] * (M+1) for _ in range(N+1)]
visited = [[0] * (M+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    lst[a][b] = 1

def bfs(i, j):
    ans = 1
    queue =deque([(i, j)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx <= N and 0 <= ty <= M and lst[tx][ty] == 1 and visited[tx][ty] == 0:
                ans += 1
                visited[tx][ty] = 1
                queue.append((tx, ty))
    return ans

res = 0
for x in range(N+1):
    for y in range(M+1):
        if visited[x][y] == 0 and lst[x][y] == 1:
            visited[x][y] = 1
            res = max(bfs(x, y), res)

print(res)
