from collections import deque

S = int(input())
visited = {}
visited[(1, 0)] = 0

def bfs():
    queue = deque([(1, 0)])
    
    while queue:
        x, c = queue.popleft()
        if x == S:
            return visited[(x, c)]

        if (x, x) not in visited.keys():
            visited[(x, x)] = visited[(x, c)] + 1
            queue.append((x, x))
        if (x+c, c) not in visited.keys():
            visited[(x+c, c)] = visited[(x, c)] + 1
            queue.append((x+c, c))
        if (x-1, c) not in visited.keys() and x > 0:
            visited[(x-1, c)] = visited[(x, c)] + 1
            queue.append((x-1, c))

print(bfs())