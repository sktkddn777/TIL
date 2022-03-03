from itertools import chain, permutations

def is_prime_num(n):
    if n == 0 or n == 1:
        return False
    else:
        for num in range(2, n):
            if n % num == 0:
                return False
        return True


def solution(numbers):
    answer = 0
    num_lst = []
    lst = list(chain.from_iterable(permutations(list(numbers), r) for r in range(1, len(numbers) + 1)))

    for num in lst:
        num = int(str(''.join(num)))
        num_lst.append(num)

    for num in set(num_lst):
        if is_prime_num(num):
            answer += 1
    return answer