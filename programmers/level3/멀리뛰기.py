def solution(n):
    lst = [0, 1, 2]

    if n < 3:
        return lst[n]

    for x in range(3, n+1):
        lst.append((lst[x-1] + lst[x-2]) % 1234567)

    return lst[-1]