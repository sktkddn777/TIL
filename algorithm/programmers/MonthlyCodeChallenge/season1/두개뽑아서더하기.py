from itertools import combinations

def solution(numbers):
    lst = list(combinations(numbers, 2))
    res = [sum(x) for x in lst]
    res = list(set(res))
    return sorted(res)

solution([2,1,3,4,1])