from collections import Counter

N = int(input())

candy_lst = []
candy_lst_rotate = []
for i in range(N):
    lst = list(input())
    candy_lst.append(lst)

candy_lst_rotate = list(zip(*candy_lst))
candy_lst_rotate = [list(x) for x in candy_lst_rotate]

res = []
for i in range(N):
    for j in range(N):
        tmp1 = candy_lst[i][j]
        tmp2 = candy_lst_rotate[i][j]
        res.append(max(Counter(candy_lst[i]).values()))
        res.append(max(Counter(candy_lst_rotate[i]).values()))
        if i != N-1:
            candy_lst[i][j] = candy_lst[i+1][j]
            candy_lst_rotate[i][j] = candy_lst_rotate[i+1][j]
            res.append(max(Counter(candy_lst[i]).values()))
            res.append(max(Counter(candy_lst_rotate[i]).values()))

        if i != 0:
            candy_lst[i][j] = candy_lst[i-1][j]
            candy_lst_rotate[i][j] = candy_lst_rotate[i-1][j]
            res.append(max(Counter(candy_lst[i]).values()))
            res.append(max(Counter(candy_lst_rotate[i]).values()))
        candy_lst[i][j] = tmp1
        candy_lst_rotate[i][j] = tmp2

print(max(res))