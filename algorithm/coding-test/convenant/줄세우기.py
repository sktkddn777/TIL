from collections import deque

N, M = map(int, input().split())
graph = {x: [] for x in range(1, N+1)}
input_g = {x: 0 for x in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    input_g[b] += 1

queue = deque()
res = []

for k,v in input_g.items():
    if v == 0:
        queue.append(k)

while queue:
    x = queue.popleft()
    res.append(x)

    for g in graph[x]:
        input_g[g] -= 1
        if input_g[g] == 0:
            queue.append(g)

print(*res)

# from collections import deque

# N, M = map(int, input().split())
# input_graph = {x: [] for x in range(1, N+1)}
# output_graph = {x: [] for x in range(1, N+1)}

# for _ in range(M):
#     a, b = map(int, input().split())
#     input_graph[b].append(a)
#     output_graph[a].append(b)

# queue = deque([])
# for k, v in input_graph.items():
#     if len(v) == 0:
#         queue.append(k)

# res = []
# while queue:
#     x = queue.popleft()
#     res.append(x)

#     for g in output_graph[x]:
#         input_graph[g].remove(x)
#         if len(input_graph[g]) == 0:
#             queue.append(g)

# for r in res:
#     print(r, end=' ')



    

