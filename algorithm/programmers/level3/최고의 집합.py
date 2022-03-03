def solution(n, s):
    a, b = s//n, s%n

    if a == 0:
        return [-1]

    lst = [a+1] * b + [a] * (n-b)
    lst = sorted(lst)
    return lst
