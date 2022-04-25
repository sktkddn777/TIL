N = int(input())
res = [str(x) for x in range(10)]

def dfs(l, word, w):
    global res
    if len(word) == l:
        res.append(word)
    for j in range(10):
        if j < w:
            dfs(l, str(word)+str(j), j)
        


for l in range(2, 11):
    n = l - 1
    for j in range(n, 10):
        dfs(l, str(j), j)

if N >= len(res):
    print(-1)
else:
    print(res[N])