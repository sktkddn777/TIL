'''
최단 경로 알고리즘 : 다익스트라 알고리즘
에 대해서 알게 되었다.

'''

from collections import deque


def solution(N, road, K):
    node = {}

    for r in road:
        node[r[0]] = node.get(r[0], []) + [(r[2], r[1])]
        node[r[1]] = node.get(r[1], []) + [(r[2], r[0])]

    data = [(float('inf'), x) for x in range(N+1)]
    data[1] = (0, 1)
    queue = deque()
    queue.append(data[1])

    while queue:
        q = queue.popleft()
        time, n = q[0], q[1]

        for x in node[q[1]]:
            if data[x[1]][0] > time + x[0]:
                data[x[1]] = (time + x[0], x[1])
                queue.append((time+x[0], x[1]))

    answer = 0
    for d in data:
        if d[0] <= K:
            answer += 1
    return answer
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))