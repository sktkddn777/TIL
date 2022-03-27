N = int(input())
dp = [0] * (N+1)
if N == 1:
  print(1)
elif N == 2:
  print(3)
else:
  dp[1], dp[2] = 1, 3
  for i in range(3, N+1):
    dp[i] = 2*dp[i-2] + dp[i-1]
  print(dp[N] % 10007)