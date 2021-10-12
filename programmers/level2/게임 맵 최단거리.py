from collections import deque


def bfs(maps):
    queue = deque()
    queue.append([0, 0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        data = queue.popleft()

        x, y = data[0], data[1]

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < len(maps) and 0 <= ty < len(maps[0]):
                if maps[tx][ty] == 1:
                    maps[tx][ty] = maps[x][y] + 1
                    queue.append([tx, ty])


def solution(maps):
    bfs(maps)
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    return answer