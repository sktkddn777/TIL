from re import L


n, k = map(int, input().split())
dp = [0] * (k+1)

coin = []
for _ in range(n):
  coin.append(int(input()))

dp[0] = 1
for x in coin:
  for y in range(x, k+1):
    dp[y] += dp[y-x]

print(dp[k])