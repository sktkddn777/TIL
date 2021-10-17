
def solution(rows, columns, queries):
    answer = []
    lst = [[x for x in range((r*columns)+1, (r*columns)+columns+1)]for r in range(rows)]

    for query in queries:
        # 왼쪽 위로 / 아래 왼쪽 / 오른 위로 / 위 가로
        x, y, dx, dy = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        first_num = lst[x][y]
        min_num = rows * columns

        for i in range(x, dx):
            lst[i][y] = lst[i+1][y]
            if lst[i][y] < min_num:
                min_num = lst[i][y]

        for i in range(y, dy):
            lst[dx][i] = lst[dx][i+1]
            if lst[dx][i] < min_num:
                min_num = lst[dx][i]

        for i in range(dx, x, -1):
            lst[i][dy] = lst[i-1][dy]
            if lst[i][dy] < min_num:
                min_num = lst[i][dy]

        for i in range(dy, y, -1):
            lst[x][i] = lst[x][i-1]
            if lst[x][i] < min_num:
                min_num = lst[x][i]

        lst[x][y+1] = first_num

        if first_num < min_num:
            min_num = first_num
        answer.append(min_num)

    return answer