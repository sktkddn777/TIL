def solution(s):
    answer = len(s)
    length = len(s)

    for i in range(1, (length // 2) + 1):
        res = ""
        loop = 1
        before_num = s[:i]

        for j in range(i, length, i):
            if before_num == s[j:j+i]:
                loop += 1
            else:
                if loop != 1:
                    res += str(loop)
                res += str(before_num)
                before_num = s[j:j+i]
                loop = 1

        if loop != 1:
            res += str(loop)
        res += before_num
        
        if len(res) < answer:
            answer = len(res)
    return answer