from itertools import combinations


def solution(relation):
    N = len(relation[0])
    key_index = list(range(N))

    keys = []
    for i in range(1, N+1):
        keys.extend(list(combinations(key_index, i)))

    not_unique = []
    for key in keys:
        is_overlap = []
        for r in relation:
            data = []
            for k in key:
                data.append(r[k])
            if data in is_overlap:
                not_unique.append(key)
                break
            else:
                is_overlap.append(data)
    keys = sorted(list(set(keys) - set(not_unique)))

    least = []
    for x in keys:
        for y in keys:
            if x!=y:
                if set(x).issubset(set(y)):
                    least.append(y)

    answer = set(keys).difference(set(least))

    return len(answer)


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])