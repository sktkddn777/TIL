N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [1] * 10

for i in range(2, N + 1):
  dp[i][0] = 1
  for j in range(1, 10):
    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 10007

print(sum(dp[N]) % 10007)