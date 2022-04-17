from collections import deque

def find_path(visited, edge_dic):
    path = []
    queue = deque([(-1, 0)])
    visited[0] = 1
    while queue:
        p, c = queue.popleft()
        path.append((p,c))
        for edge in edge_dic[c]:
            if visited[edge] == 0:
                queue.append((c, edge))
                visited[edge] = 1
    return path[::-1]

def solution(a, edges):
    edge_dic = {x:[] for x in range(len(a))}
    for edge in edges:
        edge_dic[edge[0]].append(edge[1])
        edge_dic[edge[1]].append(edge[0])
    
    visited = [0] * len(edge_dic)
    path = find_path(visited, edge_dic)
    
    res = 0
    for p in path:
        if p[0] == -1:
            break
        a[p[0]] += a[p[1]]
        res += abs(a[p[1]])
    
    if a[0] == 0:
        return res
    return -1

print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))