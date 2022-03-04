N = int(input())
cost = []
dp = []

for _ in range(N):
  cost.append(list(map(int, input().split())))
  dp.append([0,0,0])

dp[0] = cost[0]

for i in range(1, N):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[-1]))
