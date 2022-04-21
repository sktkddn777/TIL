N = int(input())
num_lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

res = []
def dfs(num, cnt):
    global add, sub, mul, div, res

    if cnt == N:
        res.append(num)
    else:
        if add > 0:
            add -= 1
            dfs(num + num_lst[cnt], cnt+1)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(num - num_lst[cnt], cnt+1)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(num * num_lst[cnt], cnt+1)
            mul += 1
        if div > 0:
            div -= 1
            dfs(int(num / num_lst[cnt]), cnt+1)
            div += 1

dfs(num_lst[0], 1)
print(max(res))
print(min(res))