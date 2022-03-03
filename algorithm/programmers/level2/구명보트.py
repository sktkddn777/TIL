from collections import deque

def solution(people, limit):
    answer = 0

    people = deque(sorted(people, reverse=True))

    while people:
        man = people.popleft()
        if people:
            if man + people[-1] <= limit:
                answer += 1
                people.pop()
            else:
                answer += 1
        else:
            answer += 1
    return answer