
def solution(n, left, right):
    lst = [[0] * n for _ in range(n)]
    t = 1
    for x in range(n):
        for y in range(n):
            lst[x][y] = lst[y][x] = t
        t += 1
    
    res = []
    for l in lst:
        res += l
    return res[left: right+1]

print(solution(3, 2, 5))