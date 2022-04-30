from collections import deque

N, K = map(int, input().split())
visited = [[-1, -1]] * (100001)
visited[N] = [0, -1]

def bfs():
    queue = deque([N])

    while queue:
        x = queue.popleft()
        lst = [2*x, x+1, x-1]
        for idx, nx in enumerate(lst):
            if 0 <= nx < 100001 and (visited[nx][0] == -1 or visited[nx][0] > visited[x][0]):
                visited[nx] = [visited[x][0] + 1, idx]
                queue.append(nx)

bfs()
print(visited[K][0])

res = []
while K != N:
    res.append(K)
    if visited[K][1] == 0:
        K //= 2
    elif visited[K][1] == 1:
        K -= 1
    else:
        K += 1
res.append(N)

print(*res[::-1])