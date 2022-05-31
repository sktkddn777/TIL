R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]

time = 1
bomb_lst = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bomb_location():
    global board
    bomb_lst = []
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'O':
                bomb_lst.append((x, y))
    return bomb_lst

def bomb(bomb_lst):
    global board
    
    for x, y in bomb_lst:
        board[x][y] = '.'
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < R and 0 <= ty < C:
                board[tx][ty] = '.'

for time in range(1, N):
    if time % 2 == 1:
        bomb_lst = bomb_location()
       
        board = [['O'] * C for _ in range(R)]
    else:
        bomb(bomb_lst)

for x in board:
    print(''.join(x))
