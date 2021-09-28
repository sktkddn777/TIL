def is_balanced(string):
    left = 0
    right = 0
    for s in string:
        if s == '(':
            left += 1
        else:
            right += 1
    if left == right:
        return True

    return False


def is_correct(bracket):
    left = 0
    right = 0
    for b in bracket:
        if b == '(':
            left += 1
        else:
            right += 1
        if right > left:
            return False

    return True


def solution(p):
    if len(p) == 0 or is_correct(p):
        return p

    answer = ""
    u = ""
    v = ""
    i = 0

    for b in p:
        u += b
        i += 1
        if is_balanced(u):
            v = p[i:]
            break

    if is_correct(u):
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        u = u[1:-1]
        for x in u:
            if x == '(':
                answer += ')'
            else:
                answer += '('

    return answer