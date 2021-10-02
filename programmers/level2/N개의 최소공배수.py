from math import gcd


def solution(arr):
    answer = 1
    for x in arr:
        answer = x * answer // gcd(answer, x)

    return answer