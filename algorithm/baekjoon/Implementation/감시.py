import copy


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv_lst = []
blind_area = float('inf')

dx = [1, 0, -1, 0]
dy = [0, 1 ,0, -1]
cctv_mode = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [0, 3], [2, 1], [2, 3]],
    4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]]
}

for x in range(N):
    for y in range(M):
        if 0 < board[x][y] < 6:
            cctv_lst.append((x, y))

def fillBoard(x, y, mode, temp_board):
    for m in mode:
        tx = x
        ty = y
        while True:
            tx += dx[m]
            ty += dy[m]
            if 0 <= tx < N and 0 <= ty < M and temp_board[tx][ty] != 6:
                if temp_board[tx][ty] == 0:
                    temp_board[tx][ty] = 7
            else:
                break

def findBlindSpot(board):
    blind_num = 0
    for x in range(N):
        blind_num += board[x].count(0)
    return blind_num

def dfs(n, board):
    global blind_area

    if n == len(cctv_lst):
        blind_area = min(blind_area, findBlindSpot(board))
    else:
        x, y = cctv_lst[n]
        mode = cctv_mode[board[x][y]]
        temp_board = copy.deepcopy(board)
        
        for m in mode:
            fillBoard(x, y, m, temp_board)
            dfs(n+1, temp_board)
            temp_board = copy.deepcopy(board)

dfs(0, board)
print(blind_area)