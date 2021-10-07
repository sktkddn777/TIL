'''
맞았는데 다른 사람의 풀이를 보고 find union으로도 풀 수 있다는 것을 알게 되었다.
from collections import deque, defaultdict
import copy

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    answer = 0

    while queue:
        v = queue.popleft()
        answer += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return answer


def solution(n, wires):
    graph = defaultdict(list)
    # defaultdict

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    answer = n

    for k in graph.keys():
        for v in graph[k]:
            new_graph = copy.deepcopy(graph)
            new_graph[k].remove(v)
            new_graph[v].remove(k)
            visited = [False] * (len(graph) + 1)
            first = bfs(new_graph, k, visited)
            second = bfs(new_graph, v, visited)
            if abs(first - second) < answer:
                 answer = abs(first - second)
    return answer


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])

'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        return find_parent(parent, parent[x])
    return x



def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return

    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, wires):
    answer_lst = []

    for i in range(n-1):
        parent = [k for k in range(n+1)]
        for j in range(n-1):
            if i == j:
                continue
            a, b = wires[j][0], wires[j][1]
            union_parent(parent, a, b)

        for m in range(1, n + 1):
            find_parent(parent, m)

        one = parent.count(1)
        two = n - one
        answer_lst.append(abs(one - two))

    return min(answer_lst)

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# https://github.com/mrapacz/disjoint-set 모듈 구현 되어있음.