'''
행 열을 바꾸면 쉽게 생각할 수 있는데
그걸 어떻게 처음부터 생각해용..?

구글링 해서 이해했움.
'''

def solution(m, n, board):
    answer = 0
    b = list(map(list, zip(*board)))

    def pang_func(b):
        pang_lst = []
        for x in range(1, n):
            for y in range(1, m):
                if b[x][y] == b[x][y-1] == b[x-1][y] == b[x-1][y-1] != '_':
                    pang_lst.extend([(x, y),(x-1,y),(x,y-1),(x-1,y-1)])

        pang_lst = list(set(pang_lst))
        for pang in pang_lst:
            b[pang[0]][pang[1]] = 0

        for i, row in enumerate(b):
            empty = ['_']*row.count(0)
            b[i] = empty + [block for block in row if block != 0]

        return len(pang_lst)

    while True:
        count = pang_func(b)
        if count == 0:
            break
        answer += count
    return answer