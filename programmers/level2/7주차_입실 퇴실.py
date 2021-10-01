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