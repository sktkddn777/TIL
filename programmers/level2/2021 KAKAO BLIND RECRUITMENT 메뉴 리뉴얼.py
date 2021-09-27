from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        order_lst = []
        for order in orders:
            order_lst.extend(list(combinations(sorted(order), c)))
        count = {}
        for o in order_lst:
            if o in count:
                count[o] += 1
            else:
                count[o] = 1

        if count:
            max_num = max(count.values())
            if max_num >= 2:
                for key, value in count.items():
                    if value == max_num:
                        answer.append(''.join(key))

    answer = sorted(answer)
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))