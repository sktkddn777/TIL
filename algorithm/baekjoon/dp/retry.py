N = int(input())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))

dp = [0] * (N+1)
for i in range(N - 1, -1, -1):
  if i + arr[i][0] > N:
    dp[i] = dp[i+1]
  else:
    dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])
print(dp[0])
