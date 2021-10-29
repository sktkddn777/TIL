from collections import deque


def solution(n, computers):
    node = {}
    for i, com in enumerate(computers):
        node[i] = [x for x in range(n) if com[x] == 1 and i != x]

    visited = [0] * n

    def bfs(root):
        queue = deque(node[root])
        visited[root] = 1

        while queue:
            data = queue.popleft()
            visited[data] = 1
            for d in node[data]:
                if visited[d] == 0:
                    queue.append(d)

    res = 0
    while 0 in visited:
        for k in node.keys():
            if visited[k] == 0:
                bfs(k)
                res += 1

    return res