N, K = map(int, input().split())

coin_lst = []
for _ in range(N):
  coin_lst.append(int(input()))

total = 0
for coin in reversed(coin_lst):
  total += K // coin
  K %= coin

print(total)