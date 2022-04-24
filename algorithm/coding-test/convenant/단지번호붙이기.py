from collections import deque

def bfs(c, lst, i, j):
    queue = deque([(i, j)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    lst[i][j] = c

    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < len(lst) and 0 <= ty < len(lst) and lst[tx][ty] == '1':
                queue.append((tx, ty))
                lst[tx][ty] = c
    return cnt

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(input()))

danzi = -1
res = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == '1':
            res.append(bfs(danzi, lst, i, j))
res.sort()
print(len(res))
for r in res:
    print(r)

