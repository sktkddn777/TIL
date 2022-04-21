g_lst = list(input())

res = 0
weight = 1
stack = []

for i in range(len(g_lst)):
    if g_lst[i] == '(':
        weight *= 2
        stack.append(g_lst[i])
    elif g_lst[i] == '[':
        weight *= 3
        stack.append(g_lst[i])
    elif g_lst[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if g_lst[i-1] == '(':
            res += weight
        weight //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if g_lst[i-1] == '[':
            res += weight
        weight //= 3
        stack.pop()

print(res)