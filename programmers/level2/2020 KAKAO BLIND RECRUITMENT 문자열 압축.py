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

    '''
    11/16 답을 안보고 풀어봤다.

    def solution(s):
    result = 1000
    N = len(s)
    half = N // 2
    division = 1
    if N == 1:
        return 1
    while division <= half:
        repeat = 1
        new_s = ''
        for i in range(N // division):
            if s[i*division:(i+1)*division] == s[(i+1)*division:(i+2)*division]:
                repeat += 1
            else:
                if repeat > 1:
                    new_s += str(repeat) + s[i*division:(i+1)*division]
                    repeat = 1
                else:
                    new_s += s[i*division:(i+1)*division]

        new_s += s[(i+1)*division:]

        if len(new_s) < result:
            result = len(new_s)
        division += 1

    return result
    '''