n = int(input())

wine = []
for _ in range(n):
  wine.append(int(input()))

dp = [0] * n

if n < 3:
  print(sum(wine[:n]))
else:
  dp[0], dp[1] = wine[0], wine[0] + wine[1]

  for i in range(2, n):
    dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2], dp[i-1])

  print(max(dp))
