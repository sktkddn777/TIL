T = int(input())

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for _ in range(T):
  n = int(input())
  x = 4
  while x <= n:
    dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
    x+=1
  print(dp[n])