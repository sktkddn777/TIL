from collections import Counter


def solution(str1, str2):

    str1 = str1.upper()
    str2 = str2.upper()

    str1_lst = []
    str2_lst = []

    for s in range(len(str1) - 1):
        if str1[s].isalpha() and str1[s+1].isalpha():
            str1_lst.append(str1[s:s+2])

    for s in range(len(str2) - 1):
        if str2[s].isalpha() and str2[s+1].isalpha():
            str2_lst.append(str2[s:s+2])

    c1 = Counter(str1_lst)
    c2 = Counter(str2_lst)

    union = list((c1 | c2).elements())
    intersection = list((c1 & c2).elements())

    if len(union) == 0:
        return 65536
    return int(len(intersection) / len(union) * 65536)

# Counter에 대해 알게 되었다.