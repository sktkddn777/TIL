from collections import deque


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    progresses = deque(progresses)
    speeds = deque(speeds)

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer