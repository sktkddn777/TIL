
N, M = map(int, input().split())
r,c,d = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
res = 1
while True:

    flag = 0
    
    for i in range(4):
    # 왼쪽에 빈칸이 있는지
        ld = (d + 3) % 4
        lx = r + dx[ld]
        ly = c + dy[ld]
        d = ld

        if 0 <= lx < N and 0 <= ly < M and visited[lx][ly] == 0 and lst[lx][ly] == 0:
            visited[lx][ly] = 1
            flag = 1
            res += 1
            r, c = lx, ly
            break
        
    
    if flag == 0:
        if lst[r - dx[d]][c - dy[d]] == 1:
            break
        
        else:
            r, c = r - dx[d], c - dy[d]

print(res)