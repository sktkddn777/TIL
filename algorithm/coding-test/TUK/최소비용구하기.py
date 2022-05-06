import sys, heapq
input = sys.stdin.readline

def findMinCost(dic, start, end):
    distance = [float('inf')] * (len(dic)+1)
    queue = [(0, start)]
    distance[start] = 0

    while queue:
        cost, cur = heapq.heappop(queue)

        if cost > distance[cur]:
            continue
        
        for x in dic[cur]:
            n_cost = cost + x[1]
            if n_cost < distance[x[0]]:
                distance[x[0]] = n_cost
                heapq.heappush(queue, (n_cost, x[0]))
    
    return distance[end]

if __name__ == '__main__':
    N = int(input())
    M = int(input())

    bus_dic = {x: [] for x in range(1, N+1)}
    for _ in range(M):
        a, b, c = map(int, input().split())
        bus_dic[a].append((b, c))
    
    start, end = map(int, input().split())
    print(findMinCost(bus_dic, start, end))