from itertools import combinations

def solution(numbers):
    answer = []
    numbers = list(map(str, numbers))
    comb = list(combinations(numbers, 2))

    for c in comb:
        answer.append(int(c[0]) + int(c[1]))

    answer = sorted(list(set(answer)))
    return answer