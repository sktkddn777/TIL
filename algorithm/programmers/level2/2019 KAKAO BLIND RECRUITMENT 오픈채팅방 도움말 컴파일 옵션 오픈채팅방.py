from collections import deque

def solution(record):
    answer = []
    user_dic = {}
    queue = deque()
    for r in record:
        if r[0] == 'L':
            io, uid = r.split()
            queue.append([uid, "님이 나갔습니다."])
        else:
            io, uid, name = r.split()

            if io == "Enter":
                queue.append([uid, "님이 들어왔습니다."])
            user_dic[uid] = name

    for q in queue:
        q[0] = user_dic[q[0]]
        answer.append(str(q[0] + q[1]))


    return answer