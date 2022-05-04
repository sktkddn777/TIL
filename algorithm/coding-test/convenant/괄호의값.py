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

# lst = list(input())

# def is_correct(lst):
#     res = 0
#     stack = []

#     tmp = 1
#     flg = 1

#     for x in lst:
#         if x == '(' or x == '[':
#             if x == '(':
#                 tmp *= 2

#             elif x == '[':
#                 tmp *= 3
#             stack.append(x)
#             flg = 1

#         else:
#             if not stack:
#                 return 0

#             if x == ')':
#                 if stack[-1] == '(' and flg:
#                     res += tmp
#                     flg = 0
#                 elif stack[-1] == '[':
#                     return 0
#                 tmp = tmp // 2
#             elif x == ']':
#                 if stack[-1] == '[' and flg:
#                     res += tmp
#                     flg = 0
#                 elif stack[-1] == '(':
#                     return 0
#                 tmp = tmp // 3
#             stack.pop()

#     if stack:
#         return 0

#     return res

# print(is_correct(lst))