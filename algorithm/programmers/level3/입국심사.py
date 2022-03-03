'''
이진 탐색.
수를 구성할 때 어떤식으로 구성해야 제일 작은 수가 나오는지
판별 완료.
but, 이진탐색을 어떻게 써야되는지 적용 못함.

지금은 이해 완료,
'''


def solution(n, times):
    left = 1
    right = max(times) * n

    while left < right:
        total = 0
        mid = (left+right)//2

        for time in times:
            total += (mid // time)

        if total >= n:
            right = mid
        else:
            left = mid + 1

    return left