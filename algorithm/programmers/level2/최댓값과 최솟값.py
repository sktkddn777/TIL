def solution(s):
    answer = ''
    lst = s.split()
    lst = list(map(int, lst))

    answer = answer + str(min(lst)) + ' '
    answer += str(max(lst))
    return answer
