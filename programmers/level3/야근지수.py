'''
고민해서 풀었는데 
힙을 사용해야 하는 문제라고 한다.

import heapq

def solution(n, works):
    answer = 0
    heap = []

    for work in works:
        heapq.heappush(heap, (-work, work))

    if n > sum(works):
        return 0

    while n > 0:
        num = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-num, num))
        n -= 1

    for h in heap:
        answer += h[1] ** 2
    return answer
    
'''

def solution(n, works):
    answer = 0
    works = sorted(works, reverse=True)

    if len(works) == 1:
        if works[0] < n:
            return 0
        else:
            return (works[0]-n) ** 2
    index = 1
    while index < len(works):

        differ = works[index-1] - works[index]

        if differ == 0:
            index += 1
        else:
            if n > index * differ:
                for i in range(index):
                    works[i] -= differ
                n -= index * differ
            else:
                break

    while n > 0:
        max_num = max(works)
        if works.count(0) == len(works):
            return 0
        works[works.index(max_num)] -= 1
        n -= 1

    for work in works:
        answer += work ** 2
    return answer
