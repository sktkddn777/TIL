'''
간단한 문제인줄 알았는데 경로가 끊어지는 경우도
고려해야한다.
이 부분은 구글링했다.
'''

def solution(tickets):
    answer = []

    course_dic = {}
    for ticket in tickets:
        course_dic[ticket[0]] = course_dic.get(ticket[0], []) + [ticket[1]]

    for key in course_dic.keys():
        course_dic[key] = sorted(course_dic[key], reverse=True)

    queue = ["ICN"]
    while queue:
        data = queue[-1]
        if data not in course_dic:
            answer.append(queue.pop())
        else:
            if len(course_dic[data]) == 0:
                answer.append(queue.pop())
            else:
                queue.append(course_dic[data].pop())
    return answer[::-1]