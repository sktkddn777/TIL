from collections import deque

N, K = map(int, input().split())
visited = [-1] * (100001)
visited[N] = 0

def bfs():
    queue = deque([N])

    while queue:
        x = queue.popleft()
        for nx in [2*x, x+1, x-1]:
            if 0 <= nx < 100001 and (visited[nx] == -1 or visited[nx] > visited[x]):
                if nx == 2*x:
                    visited[nx] = visited[x]
                else:
                    visited[nx] = visited[x] + 1
                queue.append(nx)

bfs()
print(visited[K])