def solution(s):
    answer = []

    str = ""
    boolean = False
    for data in s[1: -1]:
        if boolean:
            str += data
        if data == '{':
            boolean = True
        if data == '}':
            boolean = False

    lst = str.split('}')
    lst.pop()

    dic = {}
    for data in lst:
        dic[len(data)] = data.split(',')

    sort_dict = sorted(dic.items())

    for key, value in sort_dict:
        for v in value:
            if v not in answer:
                answer.append(v)

    answer = list(map(int, answer))
    print(answer)
    return answer