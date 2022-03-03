def solution(n, lost, reserve):
    answer = 0
    duplicate_num = set(lost).intersection(reserve)

    if duplicate_num:
        lost = list(set(lost) - duplicate_num)
        reserve = list(set(reserve) - duplicate_num)

    for student in range(1, n + 1):
        if student in lost:
            if student - 1 in reserve:
                reserve.remove(student - 1)
                answer += 1
            elif student + 1 in reserve:
                reserve.remove(student + 1)
                answer += 1
        else:
            answer += 1

    return answer