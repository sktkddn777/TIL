from collections import deque

if __name__ == '__main__':
    N = int(input())
    K = int(input())

    board = [[0] * N for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        board[a-1][b-1] = 1

    L = int(input())
    rotate_dic = {}
    for _ in range(L):
        a, b = input().split()
        rotate_dic[int(a)] = b
    
    bamm_head_dic = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0)
    }
    

    bamm = deque([(0, 0)])
    bamm_head = 0 # 뱀의 머리 방향

    res = 0
    x, y = 0, 0
    while True:
        if res in rotate_dic:
            if rotate_dic[res] == 'D':
                bamm_head = (bamm_head + 1) % 4
            else:
                bamm_head = (bamm_head - 1) % 4

        dx, dy = bamm_head_dic[bamm_head]

        x += dx
        y += dy

        if (x, y) in bamm:
            break

        if 0 <= x < N and 0 <= y < N:
            if board[x][y] == 1:
                board[x][y] = 0
            else:
                bamm.popleft()
            bamm.append((x, y))
        else:
            break

        res += 1

    print(res+1)
        