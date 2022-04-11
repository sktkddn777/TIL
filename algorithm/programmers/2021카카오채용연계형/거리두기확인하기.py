from collections import deque

def bfs(i, j, place):
    queue = deque([(i, j, 0)])
    visited = [[0] * 5 for _ in range(5)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, t = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            tt = t+1
            if 0 <= tx < 5 and 0 <= ty < 5 and visited[tx][ty] == 0:
                if place[tx][ty] == 'P':
                    if tt <= 2:
                        return 0
                elif place[tx][ty] == 'O':
                    if tt == 1:
                        queue.append((tx, ty, tt))
                visited[tx][ty] = 1
                
    return 1

def solution(places):
    res = []
    
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(i, j, place) == 0:
                        flag = 0
        
        res.append(flag)
    return res

print(solution(	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]))