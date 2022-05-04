N = int(input())
candy_lst = []
for _ in range(N):
    candy_lst.append(list(input()))
candy_lst_rotate = []
candy_lst_rotate = list(zip(*candy_lst))
candy_lst_rotate = [list(x) for x in candy_lst_rotate]

def count_logest(lst):
    count = 1
    max_c = 0

    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            count += 1
        else:
            max_c = max(max_c, count)
            count = 1

    max_c = max(max_c, count)
    return max_c

def detect(location):
    x, y = location
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    res = 0

    
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if candy_lst[x][y] != candy_lst[tx][ty]:
                candy_lst[x][y], candy_lst[tx][ty] = candy_lst[tx][ty], candy_lst[x][y]
                res = max(res, count_logest(candy_lst[x]))
                candy_lst[tx][ty], candy_lst[x][y] = candy_lst[x][y], candy_lst[tx][ty]
            if candy_lst_rotate[x][y] != candy_lst_rotate[tx][ty]:
                candy_lst_rotate[x][y], candy_lst_rotate[tx][ty] = candy_lst_rotate[tx][ty], candy_lst_rotate[x][y]
                res = max(res, count_logest(candy_lst_rotate[x]))
                candy_lst_rotate[tx][ty], candy_lst_rotate[x][y] = candy_lst_rotate[x][y], candy_lst_rotate[tx][ty]
    return res
res = 0
for x in range(N):
    for y in range(N):
        res = max(res, count_logest(candy_lst[x]))
        res = max(res, count_logest(candy_lst_rotate[y]))
        res = max(res, detect((x, y)))

print(res)