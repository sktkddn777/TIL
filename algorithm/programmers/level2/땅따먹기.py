def solution(lst):

    for i in range(1, len(lst)):
        lst[i][0] = max(lst[i-1][1], lst[i-1][2], lst[i-1][3]) + lst[i][0]
        lst[i][1] = max(lst[i - 1][0], lst[i - 1][2], lst[i - 1][3]) + lst[i][1]
        lst[i][2] = max(lst[i - 1][0], lst[i - 1][1], lst[i - 1][3]) + lst[i][2]
        lst[i][3] = max(lst[i - 1][0], lst[i - 1][1], lst[i - 1][2]) + lst[i][3]

    answer = max(lst[-1])
    return answer