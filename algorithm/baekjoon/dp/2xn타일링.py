n = int(input())

dp = [0] * 1001
dp[1], dp[2] = 1, 2
i = 3
while i <= n:
  dp[i] = (dp[i - 1] + dp[i -2]) % 10007
  i+=1
print(dp[n])