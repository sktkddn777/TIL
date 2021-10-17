def solution(n):
    lst = sorted(list(str(n)), reverse=True)
    return int(''.join(lst))