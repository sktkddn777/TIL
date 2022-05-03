from collections import deque
N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

def bfs(shark_lst):
    queue = deque(shark_lst)
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and lst[tx][ty] == 0:
                lst[tx][ty] = lst[x][y] + 1
                queue.append((tx, ty))

    res = 0
    for x in lst:
        res = max(res, max(x))
    return res - 1


shark_lst = []
for x in range(N):
    for y in range(M):
        if lst[x][y] == 1:
            shark_lst.append((x, y))

print(bfs(shark_lst=shark_lst))