N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

dp[1] = arr[1]
for i in range(2, N + 1):
  for k in range(i + 1):
    dp[i] = max(dp[i], dp[i - k] + arr[k])
print(dp[N])