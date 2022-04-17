from collections import deque

close_giho = [']', ')', '}']
open_giho = ['[', '(', '{']

def check_is_ok(lst):
    stack = []

    for l in lst:
        if l in close_giho:
            if len(stack) == 0:
                return 0

            if open_giho.index(stack.pop()) != close_giho.index(l):
                return 0
        else:
            stack.append(l)
    if len(stack) != 0:
        return 0
    return 1

def solution(s):
    res = 0
    queue = deque(list(s))
    for _ in range(len(s)):
        res += check_is_ok(queue)
        queue.append(queue.popleft())
    return res
