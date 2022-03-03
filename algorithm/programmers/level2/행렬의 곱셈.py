import numpy as np


def solution(arr1, arr2):
    answer = []
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    multi_matrix = arr1 @ arr2

    for m in multi_matrix:
        middle_lst = []
        for x in m:
            middle_lst.append(int(x))
        answer.append(middle_lst)
    return answer