from collections import deque

def check_node(wires_dic, nodes):
    queue = deque([(nodes[0], 1), (nodes[1], 2)])
    visited = [0] * (len(wires_dic) + 1)

    while queue:
        k , t= queue.popleft()
        visited[k] = t
        for v in wires_dic[k]:
            if (k == nodes[0] and v == nodes[1]) or (k == nodes[1] and v == nodes[0]):
                continue
            if visited[v] == 0:
                queue.append((v, t))
    
    return abs(visited.count(1) - visited.count(2))

def solution(n, wires):
    node = [x for x in range(1, n+1)]

    wires_dic = {x:[] for x in range(1, n+1)}
    for wire in wires:
        wires_dic[wire[0]].append(wire[1])
        wires_dic[wire[1]].append(wire[0])
    
    res = []
    for wire in wires:
        res.append(check_node(wires_dic, wire))
    
    return min(res)

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))