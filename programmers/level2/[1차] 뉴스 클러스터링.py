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

# 11/15 Counter를 안쓰고 풀어봤다. Union intersection의 중복이 허용됨을 문제를 통해 확인 잘 해줘야 한다. 
# 이 부분 때문에 시간 좀 잡아 먹었다.

'''

def Jacard(str1, str2):
    lst1, lst2 = [], []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            lst1.append(str1[i:i+2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            lst2.append(str2[i:i+2])

    union, intersection = [], []
    hap, gyo = (set(lst1) | set(lst2)), (set(lst1) & set(lst2))
    for i in gyo:
        for _ in range(min(lst1.count(i), lst2.count(i))):
            intersection.append(i)
    for i in hap:
        for _ in range(max(lst1.count(i), lst2.count(i))):
            union.append(i)

    if len(union) == 0:
        return 1

    return len(intersection)/len(union)


def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()

    n = Jacard(str1, str2)

    return int(n * 65536)

'''