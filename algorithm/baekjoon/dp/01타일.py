N = int(input())

dp = [0] * (N + 1)
if N < 3:
  print(N)
else:
  dp[1], dp[2] = 1, 2
  for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
  print(dp[N])
