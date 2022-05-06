import heapq, sys
input = sys.stdin.readline

def findMinTree(dic):
    queue = [(0, 1)]
    visited = [0] * (len(dic) + 1)
    cnt = 0
    weight = 0

    while queue:
        cost, cur = heapq.heappop(queue)
        if cnt == len(dic):
            break

        if visited[cur] == 0:
            visited[cur] = 1
            cnt += 1
            weight += cost

            for x in dic[cur]:
                if visited[x[1]] == 0:
                    heapq.heappush(queue, x)

    return weight

if __name__ == '__main__':
    V, E = map(int, input().split())
    graph_dic = {x: [] for x in range(1, V+1)}
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph_dic[a].append((c, b))
        graph_dic[b].append((c, a))
    
    print(findMinTree(graph_dic))
