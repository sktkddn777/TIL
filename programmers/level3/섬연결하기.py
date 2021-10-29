'''
크루스칼 알고리즘을 사용한다.
그냥 간단하게 간선 낮은 순으로 정렬하고

사이클 때문에 while문 하나 두고

둘 다 있으면 pass / 둘 중 하나만이라도 처음 가는 섬이면 연결
'''


def solution(n, costs):
    costs = sorted(costs, key=lambda x:x[2])
    visited = set([costs[0][0]])

    res = 0
    while len(visited) < n:
        for cost in costs:
            if cost[0] in visited and cost[1] in visited:
                continue
            if cost[0] in visited or cost[1] in visited:
                res += cost[2]
                visited.update([cost[0], cost[1]])
                break
    return res