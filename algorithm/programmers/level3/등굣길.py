def solution(m, n, puddles):
    lst = [[0] * (m+1) for _ in range(n+1)]

    puddles = [[q,p] for [p,q] in puddles]
    lst[1][1] = 1

    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1:
                continue
            if [x,y] not in puddles:
                lst[x][y] = (lst[x-1][y] + lst[x][y-1]) % 1000000007
            else:
                lst[x][y] = 0

    return lst[-1][-1]