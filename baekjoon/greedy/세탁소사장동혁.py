T = int(input())

change_lst = [25, 10, 5, 1]

for _ in range(T):
  change = int(input())

  for i in range(4):
    print(change // change_lst[i], end=' ')
    change %= change_lst[i]
  print()