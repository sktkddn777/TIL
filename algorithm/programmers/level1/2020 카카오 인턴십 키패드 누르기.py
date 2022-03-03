def solution(numbers, hand):
    answer = ''
    num_dic = {
        1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
        4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
        7 : [2, 0], 8 : [2, 1], 9 : [2, 2], 0 : [3, 1]
    }

    left_num = [1, 4, 7]
    right_num = [3, 6, 9]

    left_hand = [3, 0]
    right_hand = [3, 2]

    for num in numbers:
        if num in left_num:
            answer += 'L'
            left_hand = num_dic[num]

        elif num in right_num:
            answer += 'R'
            right_hand = num_dic[num]
        else:
            right_distance = abs(right_hand[0] - num_dic[num][0]) + abs(right_hand[1] - num_dic[num][1])
            left_distance = abs(left_hand[0] - num_dic[num][0]) + abs(left_hand[1] - num_dic[num][1])
            if right_distance > left_distance:
                answer += 'L'
                left_hand = num_dic[num]
            elif right_distance < left_distance:
                answer += 'R'
                right_hand = num_dic[num]
            else:
                if hand == "right":
                    answer += 'R'
                    right_hand = num_dic[num]
                else:
                    answer += 'L'
                    left_hand = num_dic[num]
    return answer