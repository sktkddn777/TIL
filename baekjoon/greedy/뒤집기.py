S = input()
lst = [0, 0]

temp = S[0]
lst[int(temp)] += 1
for s in S:
  if s != temp:
    temp = s
    lst[int(temp)] += 1

print(min(lst))