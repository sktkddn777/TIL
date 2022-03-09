T = int(input())

for _ in range(T):
  N = int(input())
  dp = [0] * (N + 1)
  if N < 3:
    print(1)
  else:
    dp[1], dp[2] = 1, 1
    for i in range(3, N+1):
      dp[i] = dp[i-2] + dp[i-3]
    print(dp[N])

