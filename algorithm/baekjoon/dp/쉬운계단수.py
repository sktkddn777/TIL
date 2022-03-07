N = int(input())

dp = [[1] * 10 for _ in range(N)]
dp[0][0] = 0

for i in range(1, N):
  dp[i][0] = dp[i-1][1]
  dp[i][9] = dp[i-1][8]
  for y in range(1, 9):
    dp[i][y] = dp[i-1][y-1] + dp[i-1][y+1]

print(sum(dp[N-1]) % 1000000000)