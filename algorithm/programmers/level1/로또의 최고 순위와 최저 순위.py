def solution(lottos, win_nums):
    zero = 0
    correct = 0

    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto in win_nums:
            correct += 1
    
    if correct > 1:
        rank = 7 - correct
        highest = rank - zero
    elif correct == 1:
        rank = 6
        highest = rank - zero
    else:
        rank = 6
        if zero == 0:
            highest = 6
        else:
            highest = 7 - zero

    answer = [highest, rank]

    return answer