def solution(clothes):
    answer = 1
    dic = {}
    for data in clothes:
        if data[1] in dic:
            dic[data[1]] += 1
        else:
            dic[data[1]] = 1

    for value in dic.values():
        answer *= (value + 1)
    answer -= 1
    return answer