from collections import deque


N, M = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(list(input()))

res = [[0] * M for _ in range(N)]
res[0][0] = 1
def bfs():
    queue = deque([(0, 0)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and lst[tx][ty] == '1' and res[tx][ty] == 0:
                res[tx][ty] = res[x][y] + 1
                queue.append((tx, ty))

bfs()
print(res[N-1][M-1])