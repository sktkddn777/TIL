import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

res = 0

def dfs(m, x, y):
    global res

    if x == (N-1) and y == (N-1):
        res += 1
    
    if x+1 < N and y+1 < N:
        if lst[x+1][y] == 0 and lst[x][y+1] == 0 and lst[x+1][y+1] == 0:
            dfs(3, x+1, y+1)
    
    if m == 1 or m == 3:
        if y+1 < N and lst[x][y+1] == 0:
            dfs(1, x, y+1)
    
    if m == 2 or m == 3:
        if x+1 < N and lst[x+1][y] == 0:
            dfs(2, x+1, y)

# 1: 가로 2:세로 3:대각
dfs(1, 0, 1)
print(res)