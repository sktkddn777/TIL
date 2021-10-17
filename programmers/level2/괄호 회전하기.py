from collections import deque

def is_correct(gualho):
    stack = []
    queue = deque(list(gualho))
    correct_dic = {
        '[':']',
        '{':'}',
        '(':')',
    }

    while queue:
        data = queue.popleft()
        if data in correct_dic.keys():
            stack.append(data)
        else:
            if len(stack) == 0:
                return False
            if correct_dic[stack.pop()] != data:
                return False
    if len(stack) > 0:
        return False
    return True

def solution(s):
    answer = 0
    for _ in range(len(s)):
        if is_correct(s):
            answer += 1

        s = s[1:] + s[0]
    return answer