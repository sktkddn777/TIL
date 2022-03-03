def solution(N, stages):
    answer = []
    player_num = len(stages)
    fail_rate = {}
    for s in range(1, N + 1):
        if player_num == 0:
            fail_rate[s] = 0
        else:
            count = stages.count(s)
            fail_rate[s] = count / player_num
            player_num -= count
    sorted_lst = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)
    for data in sorted_lst:
        answer.append(data[0])
    return answer