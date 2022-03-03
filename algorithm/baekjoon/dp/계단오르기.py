N = int(input())

stair = [0] *(N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
  stair[i] = int(input())

if N == 1:
  print(stair[1])
else:
  dp[1], dp[2] = stair[1], stair[1] + stair[2]
  for i in range(3, N+1):
    dp[i] = max((stair[i] + stair[i-1] + dp[i-3]), (stair[i] + dp[i-2]))

  print(dp[N])


