
from collections import deque


N, M = map(int, input().split())
lst = []
for _ in range(M):
    lst.append(list(input()))
visited = [[0] * N for _ in range(M)]

def bfs(v, cor):
    ans = 1
    queue = deque([cor])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < M and 0 <= ty < N and visited[tx][ty] == 0 and lst[tx][ty] == v:
                queue.append((tx, ty))
                visited[tx][ty] = 1
                ans += 1
    return ans ** 2

res_W = 0
res_B = 0

for m in range(M):
    for n in range(N):
        if lst[m][n] == 'W' and visited[m][n] == 0:
            visited[m][n] = 1
            res_W += bfs('W', (m, n))
        elif lst[m][n] == 'B' and visited[m][n] == 0:
            visited[m][n] = 1
            res_B += bfs('B', (m, n))

print(res_W, res_B)