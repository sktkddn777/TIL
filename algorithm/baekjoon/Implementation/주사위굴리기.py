N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commandList = list(map(int, input().split()))

dice = [0] * 6
command_dic = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

def turnDice(dice, command):
    if command == 1:
        a, b, c, d, e, f = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif command == 2:
        a, b, c, d, e, f = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif command == 3:
        a, b, c, d, e, f = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    else:
        a, b, c, d, e, f = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    
    dice = [a, b, c, d, e, f]
    return dice

for command in commandList:
    dx, dy = command_dic[command]
    
    if 0 <= x+dx < N and 0 <= y+dy < M:
        dice = turnDice(dice, command)
        x += dx
        y += dy
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0

        print(dice[0])
    else:
        continue