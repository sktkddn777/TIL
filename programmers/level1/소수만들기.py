import itertools
import math


def is_prime_number(n):
    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [i for i in range(2, n + 1) if array[i]]


def solution(nums):
    answer = 0
    sum_lst = []
    num_lst = itertools.combinations(nums, 3)
    for lst in num_lst:
        sum_lst.append(sum(lst))
    prime_num = is_prime_number(max(sum_lst))

    for data in sum_lst:
        if data in prime_num:
            answer += 1
    return answer