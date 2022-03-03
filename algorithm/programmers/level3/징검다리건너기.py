'''
이분탐색으로 푸는 방법은 생각을 못했다...

다시 풀어봐야 한다.

구글링을 통해 겨우 이해는 했지만, 다시 해야한다.
'''

def solution(stones, k):
    left, right = 1, 200000000

    while left <= right:
        mid = (left + right) // 2
        blank = 0
        for stone in stones:
            if stone <= mid:
                blank += 1
                if blank == k:
                    break
            else:
                blank = 0

        if blank != k:
            left = mid + 1
        else:
            right = mid - 1

    return left