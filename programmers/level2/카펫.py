def solution(brown, yellow):
    answer = []
    yellow_lst = []

    for y in range(yellow, 0, -1):
        if yellow % y == 0 and (yellow // y) <= y:
            yellow_lst.append([y, yellow // y])

    for data in yellow_lst:
        if (data[0] + data[1]) * 2 + 4 == brown:
            answer = [data[0] + 2, data[1] + 2]
    return answer