from collections import deque
def solution(s):
    s = deque(s)
    stack = []

    while s:
        if stack:
            if s[0] == stack[-1]:
                stack.pop()
                s.popleft()
            else:
                stack.append(s.popleft())
        else:
            stack.append(s.popleft())

    if stack:
        return 0
    else:
        return 1