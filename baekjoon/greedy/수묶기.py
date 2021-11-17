N = int(input())

minus_lst = []
plus_lst = []

for _ in range(N):
  n = int(input())
  if n > 0:
    plus_lst.append(n)
  else:
    minus_lst.append(n)

plus_lst = sorted(plus_lst,reverse=True)
minus_lst = sorted(minus_lst)

total = 0
idx = 0
for i in range(0, len(plus_lst)-1, 2):
  if plus_lst[i] == 1 or plus_lst[i+1] == 1:
    break
  total += plus_lst[i] * plus_lst[i+1]
  idx += 1
total += sum(plus_lst[idx*2:])

idx = 0
for i in range(0, len(minus_lst)-1, 2):
  total += minus_lst[i] * minus_lst[i+1]
  idx += 1
total += sum(minus_lst[idx*2:])

print(total)