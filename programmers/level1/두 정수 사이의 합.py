def solution(a, b):
    if a>b:
        a, b = b, a
    res = 0
    for i in range(a, b+1):
        res += i

    return res