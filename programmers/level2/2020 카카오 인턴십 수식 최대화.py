'''
실패한 코드

from itertools import permutations
from collections import deque


def solution(expression):
    answer = 0
    operator = ['*', '+', '-']
    num_lst = []
    oper_lst = []
    expression_lst = []

    num = ''
    for ex in expression:
        if ex in operator:
            expression_lst.append(int(num))
            expression_lst.append(ex)
            oper_lst.append(ex)
            num = ''
        else:
            num += ex
    expression_lst.append(int(num))
    permu = list(permutations(list(set(oper_lst)), len(set(oper_lst))))
    
    for per in permu:
        stack = deque(list(per))
        middle_lst = expression_lst
        while stack:
            oper = stack.popleft()
            for i in range(len(middle_lst)):
                try:
                    if middle_lst[i] == oper:
                        if oper == '-':
                            middle_lst[i - 1] = middle_lst[i - 1] - middle_lst[i + 1]
                        elif oper == '+':
                            middle_lst[i - 1] = middle_lst[i - 1] + middle_lst[i + 1]
                        else:
                            middle_lst[i - 1] = middle_lst[i - 1] * middle_lst[i + 1]
                        middle_lst.pop(i)
                        middle_lst.pop(i)
                except:
                    break

        num = abs(middle_lst[0])
        if num > answer:
            answer = num

    return answer'''



from itertools import permutations
from collections import deque

def operation(n1, n2, op):
    if op == '+':
        return str(int(n1) + int(n2))
    elif op == '-':
        return str(int(n1) - int(n2))
    else:
        return str(int(n1) * int(n2))


def calculate(exp, op):
    lst = deque()
    num = ''

    for e in exp:
        if e in op:
            lst.append(num)
            lst.append(e)
            num = ''
        else:
            num += e
    lst.append(num)

    for o in op:
        stack = deque()
        while lst:
            num = lst.popleft()
            if num == o:
                stack.append(operation(stack.pop(), lst.popleft(), num))
            else:
                stack.append(num)
        lst = stack
    return abs(int(lst[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))

    result = []
    for i in op:
        result.append(calculate(expression, i))

    return max(result)


