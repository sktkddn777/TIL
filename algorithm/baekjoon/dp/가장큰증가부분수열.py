N = int(input())
dp = [0] * N
arr = list(map(int, input().split()))

dp[0] = arr[0]

for i in range(1, N):
  dp[i] = arr[i]
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))