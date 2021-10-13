def trans(n, num):
    show = '0123456789ABCDEF'
    res = ''
    if num == 0:
        return '0'

    while num>0:
        res = show[num % n] + res
        num //= n
    return res


def solution(n, t, m, p):
    answer = ''
    word = ''
    num = 0

    while len(word) < (t*m) + 1:
        word += trans(n, num)
        num += 1

    for _ in range(t):
        answer += word[p - 1]
        p += m
    return answer
