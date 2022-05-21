from collections import deque
import sys
input = sys.stdin.readline

MAX_DISTANCE = 20
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

remain_fish = 0
fish_pos = []
shark_size = 2

for x in range(N):
    for y in range(N):
        if 0 < board[x][y] < 7:
            fish_pos.append([x, y])
            remain_fish += 1
        elif board[x][y] == 9:
            shark_x, shark_y = x, y

board[shark_x][shark_y] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1 ,-1]

def bfs(shark_x, shark_y):
    queue = deque([(shark_x, shark_y, 0)])

    visited = [[0] * N for _ in range(N)]
    visited[shark_x][shark_y] = 1

    fish_distance = []
    min_dist = MAX_DISTANCE

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < N and 0 <= ty < N and visited[tx][ty] == 0:
                if board[tx][ty] <= shark_size:
                    visited[tx][ty] = 1

                    if 0 < board[tx][ty] < shark_size:
                        fish_distance.append((d+1, tx, ty))
                        min_dist = d+1

                    if d+1 < min_dist:
                        queue.append((tx, ty, d+1))
        
    if fish_distance:
        fish_distance.sort()
        return fish_distance[0]
        
    return 0


res = 0
shark_eat = 0
while remain_fish:
    shark_info = bfs(shark_x, shark_y)
    
    if shark_info == 0:
        break
    res += shark_info[0]
    shark_x, shark_y = shark_info[1], shark_info[2]
    remain_fish -= 1
    shark_eat += 1

    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0
    board[shark_x][shark_y] = 0
    
print(res)

