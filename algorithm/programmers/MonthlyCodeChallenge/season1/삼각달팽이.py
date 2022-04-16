def solution(n):
    lst = []
    num = 0

    for i in range(1, n+1):
        lst.append([0] * i)
        num += i
    
    x, y = 0, 0
    flg = 1
    lst[0][0] = 1
    for i in range(2, num+1):
        if flg == 1:
            x += 1
            if x == n-1 or lst[x+1][y] != 0:
                flg = 2
            

        elif flg == 2:
            y += 1
            if y == n-1 or lst[x][y+1] != 0:
                flg = 3
            
        else:
            x -= 1
            y -= 1
            if lst[x-1][y-1] != 0:
                flg = 1
            
        lst[x][y] = i
    
    res = []
    for i in range(n):
        res += lst[i]
    return res

solution(5)