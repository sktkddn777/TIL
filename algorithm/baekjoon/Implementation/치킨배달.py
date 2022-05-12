from itertools import combinations

def findDistance(home, chicken):
    res = 0
    for h in home:
        tmp = 50
        for c in chicken:
            tmp = min(tmp, abs(h[0]-c[0]) + abs(h[1]-c[1]))
        res += tmp
    return res


N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))


home_lst = []
chicken_lst = []
for x in range(N):
    for y in range(N):
        if lst[x][y] == 2:
            chicken_lst.append([x, y])
        elif lst[x][y] == 1:
            home_lst.append([x, y])

comb_chicken_lst = list(combinations(chicken_lst, M))

res= float('inf')
for chicken in comb_chicken_lst:
    res = min(res, findDistance(home_lst, chicken))

print(res)
