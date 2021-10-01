def solution(answers):
    answer = []
    lst = [0, 0, 0]
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, num in enumerate(answers):
        if num1[(i % 5)] == answers[i]:
            lst[0] += 1
        if num2[(i % 8)] == answers[i]:
            lst[1] += 1
        if num3[(i % 10)] == answers[i]:
            lst[2] += 1

    max_num = max(lst)
    for i, num in enumerate(lst):
        if num == max_num:
            answer.append(i + 1)

    return answer