def solution(a):
    balloon_dic = dict.fromkeys(a, 0)
    stack = []

    for key in balloon_dic.keys():
        if len(stack) == 0:
            stack.append(key)

        else:
            if key > stack[-1]:
                balloon_dic[key] += 1
            else:
                while len(stack) > 0:
                    if key > stack[-1]:
                        balloon_dic[key] += 1
                        break
                    else:
                        balloon_dic[stack[-1]] += 1
                        if balloon_dic[stack[-1]] == 2:
                            stack.pop()
                        else:
                            break

            stack.append(key)
    return len(stack)