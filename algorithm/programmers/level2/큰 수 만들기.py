def solution(number, k):
    stack = []

    for n in number:
        if not stack:
            stack.append(n)
        else:
            if k > 0:
                while stack[-1] < n:
                    k -= 1
                    stack.pop()
                    if not stack or k <= 0:
                        break
                stack.append(n)
            else:
                stack.append(n)

    answer = stack[:-k] if k > 0 else stack
    return ''.join(answer)