'''
정확성과 효율성을 모두 따져야 하는 문제이다.
정확성은 맞췄지만 효율성에서는 모두 틀림으로 나왔다.
def is_right(info, query):
    applicant = info.split(' ')
    condition = query.split(' ')
    and_lst = {'and'}
    condition = [i for i in condition if i not in and_lst]

    for i in range(len(applicant) - 1):
        if applicant[i] == condition[i] or condition[i] == '-':
            pass
        else:
            return False

    if int(condition[4]) > int(applicant[4]):
        return False

    return True


def solution(info, query):
    answer = [0] * len(query)
    for idx, que in enumerate(query):
        for applicant in info:
            if is_right(applicant, que):
                answer[idx] += 1

    return answer
'''
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    db = {}

    for i in info:
        temp = i.split(' ')
        score = int(temp.pop())

        for n in range(5):
            comb = list(combinations(range(4), n))
            for c in comb:
                temp_copy = temp.copy()
                for x in c:
                    temp_copy[x] = '-'
                changed_temp = '/'.join(temp_copy)
                if changed_temp in db:
                    db[changed_temp].append(score)
                else:
                    db[changed_temp] = [score]

    for value in db.values():
        value.sort()

    for q in query:
        condition = [i for i in q.split() if i != 'and']
        cond = '/'.join(condition[:-1])
        cond_score = int(condition[-1])

        if cond in db:
            answer.append(len(db[cond]) - bisect_left(db[cond], cond_score, lo=0, hi=len(db[cond])))
        else:
            answer.append(0)

    return answer
print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))

# 어려웠다. 한번 더 생각해봐야할 듯 하다.
# 이진탐색 라이브러리에 대해 알게 되었다.
