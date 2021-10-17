def solution(d, budget):
    answer = 0
    d = sorted(d)

    sum_d = 0
    for x in d:
        if x + sum_d > budget:
            break
        sum_d += x
        answer += 1
    return answer