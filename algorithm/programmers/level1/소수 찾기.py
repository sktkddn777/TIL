def is_prime_number(n):
    array = [True for i in range(n+1)]
    # 에라토스테네스의 체
    for i in range(2, int(n ** 1/2) + 1):
        if array[i]:

            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]


def solution(n):
    answer = len(is_prime_number(n))

    return answer