'''
시간초과 나서 틀린 문제.

from collections import deque
from itertools import combinations


def solution(enter, leave):
    answer = []
    meeting_room = []
    middle_lst = []
    enter = deque(enter)

    leave_num = 0

    while leave_num < len(leave):

        while leave_num < len(leave):
            if leave[leave_num] in meeting_room:
                lst = [x for x in meeting_room]
                middle_lst.append(list(combinations(lst, 2)))
                meeting_room.remove(leave[leave_num])
                leave_num += 1
            else:
                break

        if enter:
            enter_man = enter.popleft()
            meeting_room.append(enter_man)

    for data in middle_lst:
        for x in data:
            if x not in answer:
                answer.append(x)

    result = [0] * len(leave)

    for a in answer:
        result[a[0] - 1] += 1
        result[a[1] - 1] += 1
    return result
'''

from collections import deque


def solution(enter, leave):
    meeting_room = []
    result = [0] * len(leave)
    enter = deque(enter)
    leave = deque(leave)

    while leave:
        if not meeting_room:
            meeting_room.append(enter.popleft())

        while enter and leave[0] not in meeting_room:
            meeting_room.append(enter.popleft())

        leave_man = leave.popleft()
        meeting_room.remove(leave_man)

        for meet in meeting_room:
            if leave_man != meet:
                result[meet-1] += 1
                result[leave_man - 1] += 1

    return result
