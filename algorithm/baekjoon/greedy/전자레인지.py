T = int(input())

time_lst = [300, 60, 10]
res = []

for time in time_lst:
  res.append(T // time)
  T %= time

if T != 0:
  print('-1')
else:
  for x in res:
    print(x, end=' ')