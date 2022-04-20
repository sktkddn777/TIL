lier = []

for i in range(8):
    for j in range(i+1, 9):
        lier.append((i, j))

little_lst = []
for _ in range(9):
    little_lst.append(int(input()))

total = sum(little_lst)
for l in lier:
    if 100 == total - (little_lst[l[0]] + little_lst[l[1]]):
        little_lst[l[0]], little_lst[l[1]] = 0, 0
        break

little_lst.sort()
for x in little_lst[2:]:
    print(x)
