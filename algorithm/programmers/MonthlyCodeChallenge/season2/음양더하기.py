def solution(absolutes, signs):
    res = 0
    for i in range(len(signs)):
        if signs[i]:
            res += absolutes[i]
        else:
            res -= absolutes[i]
    return res