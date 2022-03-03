
def solution(n):
    answer = []

    lst = [[0] * x for x in range(1, n + 1)]

    ping = 1
    x, y = 0, 0
    sum_n = n*(n+1)//2

    while ping <= sum_n:
        while True:
            if x >= len(lst) or lst[x][y] != 0:
                x -= 1
                break
            lst[x][y] = ping
            x += 1
            ping += 1
        y += 1
        while True:
            if y >= len(lst) or lst[x][y] != 0:
                y -= 1
                break
            lst[x][y] = ping
            y += 1
            ping += 1
        x -= 1
        y -= 1
        while True:
            if x <= 0 or lst[x][y] != 0:
                x += 1
                y += 1
                break
            lst[x][y] = ping
            x -= 1
            y -= 1
            ping += 1
        x += 1
    # print(x, y)
    # lst[x][y] = ping

    for l in lst:
        answer.extend(l)
    return answer


print(solution(4))
