from itertools import permutations


def check(uid, bid):
    for i in range(len(bid)):
        boolean = False
        if len(uid[i]) == len(bid[i]):
            for d in range(len(bid[i])):
                if bid[i][d] != '*':
                    if bid[i][d] != uid[i][d]:
                        boolean = True
                        break
            if boolean:
                return False
        else:
            return False
    return True


def solution(user_id, banned_id):
    N = len(banned_id)
    id_lst = list(map(','.join, permutations(user_id, N)))
    data_lst = []
    for i in id_lst:
        data = i.split(',')
        if check(data, banned_id):
            if sorted(data) not in data_lst:
                data_lst.append(sorted(data))

    return len(data_lst)