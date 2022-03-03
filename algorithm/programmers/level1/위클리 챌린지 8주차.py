def solution(sizes):
    garo_lst = []
    sero_lst = []

    for size in sizes:
        garo_lst.append(size[0])
        sero_lst.append(size[1])

    max_garo = max(garo_lst)
    max_sero = max(sero_lst)

    if max_garo >= max_sero:
        for i in range(len(sizes)):
            if garo_lst[i] < sero_lst[i]:
                garo_lst[i], sero_lst[i] = sero_lst[i], garo_lst[i]

    else:
        for i in range(len(sizes)):
            if garo_lst[i] > sero_lst[i]:
                garo_lst[i], sero_lst[i] = sero_lst[i], garo_lst[i]

    answer = max(garo_lst) * max(sero_lst)
    return answer