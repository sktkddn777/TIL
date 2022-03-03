from collections import defaultdict
from collections import deque

def solution(n, edge):
    lst = [0] * (n+1)
    node_dic = defaultdict(list)

    for e in edge:
        node_dic[e[0]].append(e[1])
        node_dic[e[1]].append(e[0])

    queue = deque([1])
    lst[1] = 1

    while queue:
        node = queue.popleft()

        for d in node_dic[node]:
            if lst[d] == 0:
                lst[d] = lst[node] + 1
                queue.append(d)

    return lst.count(max(lst))