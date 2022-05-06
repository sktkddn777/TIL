from collections import deque

def findChonsu(dic, start, end):
    visited = [0] * (len(dic)+1)
    visited[start] = 1

    queue = deque([(start, 0)])
    while queue:
        node, cnt = queue.popleft()
        if node == end:
            return cnt

        for x in dic[node]:
            if visited[x] == 0:
                queue.append((x, cnt + 1))
                visited[x] = 1
    return -1

if __name__ == "__main__":
    n = int(input())
    num1, num2 = map(int, input().split())
    edge_num = int(input())
    edge_dic = {x: [] for x  in range(1, n+1)}

    for _ in range(edge_num):
        a, b = map(int, input().split())
        edge_dic[a].append(b)
        edge_dic[b].append(a)
    
    print(findChonsu(edge_dic, num1, num2))
    
    