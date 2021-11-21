'''

'''

N, L = map(int, input().split())

pipe_lst = list(map(int, input().split()))
pipe_lst.sort()

res = 1
start = pipe_lst[0]


for pipe in pipe_lst:
    if pipe - start >= L:
        res += 1
        start = pipe

print(res)