from collections import deque
import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited):
    queue = deque([(x, y)])

    group = [(x, y)]
    group_sum = board[x][y]
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < N and 0 <= ty < N and visited[tx][ty] == 0:
                if L <= abs(board[x][y]-board[tx][ty]) <= R:
                    visited[tx][ty] = 1
                    group.append((tx, ty))
                    group_sum += board[tx][ty]
                    queue.append((tx, ty))

    for g in group:
        board[g[0]][g[1]] = int(group_sum / len(group))

    if len(group) == 1:
        return 0

    return 1

res = 0
while True:
    visited = [[0] * N for _ in range(N)]
    groups = []
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                group = bfs(x, y, visited)
                if group:
                    groups.append((group))

    if len(groups) == 0:
        break
    res += 1

print(res)