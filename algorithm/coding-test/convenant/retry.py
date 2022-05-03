
N = int(input())
num_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))

res_max = -float('inf')
res_min = float('inf')

def dfs(num, cnt):
    global res_max, res_min
    if cnt == N:
        res_max = max(res_max, num)
        res_min = min(res_min, num)
    else:
        for i, x in enumerate(oper_lst):
            if x > 0:
                if i == 0:
                    oper_lst[i] -= 1
                    dfs(num + num_lst[cnt], cnt+1)
                    oper_lst[i] += 1
                elif i == 1:
                    oper_lst[i] -= 1
                    dfs(num - num_lst[cnt], cnt+1)
                    oper_lst[i] += 1
                elif i == 2:
                    oper_lst[i] -= 1
                    dfs(num * num_lst[cnt], cnt+1)
                    oper_lst[i] += 1
                else:
                    oper_lst[i] -= 1
                    dfs(int(num / num_lst[cnt]), cnt+1)
                    oper_lst[i] += 1

dfs(num_lst[0], 1)
print(res_max)
print(res_min)
