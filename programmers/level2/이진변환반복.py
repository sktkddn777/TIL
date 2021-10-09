def solution(s):
    answer = [0, 0]
    zero_count = 0
    while len(s) > 1:
        one_count = 0
        for x in s:
            if x == '0':
                zero_count += 1
            else:
                one_count += 1
        s = '{}'.format(bin(one_count)[2:])
        answer[0] += 1
    answer[1] = zero_count
    return answer