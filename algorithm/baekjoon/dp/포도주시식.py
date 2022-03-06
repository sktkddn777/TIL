n = int(input())
podoju = []
dp = [0] * n
for _ in range(n):
  podoju.append(int(input()))

if n == 1:
  dp[0] = podoju[0]
elif n == 2:
  dp[0], dp[1] = podoju[0], podoju[0] + podoju[1]
else:
  dp[0], dp[1] = podoju[0], podoju[0] + podoju[1]
  for i in range(2, n):
    dp[i] = max(dp[i-2] + podoju[i] , dp[i-3] + podoju[i-1] + podoju[i], dp[i-1])

print(max(dp))

