'''
factorial 규칙이 있는건 찾았지만,

어떤식으로 접근해야되는지는 해결하지 못했다.
몫과 나머지를 통해 인덱스를 구한다는 것은 어떻게 생각하는거지..??
'''

from math import factorial


def solution(n, k):
    answer = []
    line = [x for x in range(1, n+1)]

    while line:
        a, b = k // factorial(n-1), k % factorial(n-1)
        if b == 0:
            a -= 1
        answer.append(line.pop(a))
        n -= 1
        k = b

    return answer