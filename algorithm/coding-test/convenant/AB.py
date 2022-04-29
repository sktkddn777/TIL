
A, B = map(int, input().split())

res = []
def dfs(n, cnt):
    global res
    if n == B:
        res.append(cnt)
    
    if (n*10)+1 <= B:
        dfs((n*10)+1, cnt+1)
    if (n*2) <= B:
        dfs(n*2, cnt+1)

dfs(A, 1)
if len(res) > 0:
    print(min(res))
else:
    print(-1)