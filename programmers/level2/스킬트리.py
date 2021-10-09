from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        boolean = True
        todo = deque(list(skill))
        for t in tree:
            if t in todo and len(todo) > 0:
                if t == todo[0]:
                    todo.popleft()
                else:
                    boolean = False
        if boolean:
            answer += 1

    return answer