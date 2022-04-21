H, W = map(int, input().split())

lst = [[0] * W for _ in range(H)]
block_lst = list(map(int, input().split()))

for i in range(W):
    for j in range(block_lst[i]):
        lst[H-1-j][i] = 1


res = 0
for i in range(H):
    tmp = 0
    flg = 0
    for j in range(W):
        if not flg and lst[i][j] == 1:
            flg = 1
        elif flg and lst[i][j] == 0:
            tmp += 1
        elif flg and lst[i][j] == 1 and tmp != 0:
            res += tmp
            tmp = 0

print(res)