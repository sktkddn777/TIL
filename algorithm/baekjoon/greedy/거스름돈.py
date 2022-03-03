N = int(input())
N = 1000 - N
money_lst = [500, 100, 50, 10, 5, 1]

total = 0

for money in money_lst:
  if N // money > 0:
    total += N // money
    N %= money

print(total)