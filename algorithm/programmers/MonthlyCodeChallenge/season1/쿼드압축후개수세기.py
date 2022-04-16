zero_count = 0
one_count = 0

def dfs(lst):
    global zero_count
    global one_count

    N = len(lst)
    k = lst[0][0]
    flg = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] != k:
                flg = 1
    
    if flg:
        mid = int(N/2)
        dfs(list(x[:mid] for x in lst[:mid]))
        dfs(list(x[mid:] for x in lst[:mid]))
        dfs(list(x[:mid] for x in lst[mid:]))
        dfs(list(x[mid:] for x in lst[mid:]))
    else:
        if k == 0:
            zero_count += 1
        else:
            one_count += 1

def solution(arr):
    dfs(arr)

    return [zero_count, one_count]

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])