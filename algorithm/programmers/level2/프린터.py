from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while len(priorities) > 0:
        if priorities[0] == max(priorities):
            if location == 0:
                break
            priorities.popleft()
            answer += 1
            location -= 1

        else:
            num = priorities.popleft()
            priorities.append(num)
            if location > 0:
                location -= 1
            else:
                location = len(priorities) - 1
    answer += 1
    return answer

# 프로그래머스 보고 추가한 내용
# def solution(priorities, location):
#     queue = [(i, p) for i, p in enumerate(priorities)]
#     answer = 0
#     queue = deque(queue)
#     while True:
#         cur = queue.popleft()
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer