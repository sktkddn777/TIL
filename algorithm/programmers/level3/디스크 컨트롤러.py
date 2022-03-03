'''
heap에 대해서 공부하고 도전했는데
문제 구현 능력이 떨어진다.

더 생각해보고 풀어야 한다.
(start, now를 써서 문제 푸는방법)
'''


import heapq


def solution(jobs):
    heap = []
    answer, start, now, i = 0, -1, 0, 0

    while i < len(jobs):

        for job in jobs:
            if start<job[0]<=now:
                heapq.heappush(heap, (job[1], job[0]))

        if len(heap) > 0:
            data = heapq.heappop(heap)
            start = now
            now += data[0]
            answer += (now - data[1])
            i += 1
        else:
            now += 1
    return int(answer/len(jobs))