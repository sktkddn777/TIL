from collections import deque

def ripe(lst, visited, queue):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tmp = queue.popleft()
    x, y = tmp[0], tmp[1]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < M:
            if visited[tx][ty] == 0 and lst[tx][ty] == 0:
                queue.append([tx, ty])
                visited[tx][ty] = 1
                lst[tx][ty] = 1

def check_lst(lst):
    for i in range(len(lst)):
        if 0 in lst[i]:
            return 0
    return 1

M, N = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]

ans = 0
queue = deque([])
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = 1

while queue:
    queue_len = len(queue)
    for i in range(queue_len):
        ripe(lst, visited, queue)
    ans += 1

if check_lst(lst):
    print(ans - 1)
else:
    print(-1)