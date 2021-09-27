from math import gcd


def solution(w,h):
    num = gcd(w, h)

    if num == 1:
        answer = ((w * h) - (w + h - 1))
    else:
        answer = int((w * h) - num * ((w + h)/num - 1))

    return answer