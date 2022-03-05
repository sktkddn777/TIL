N = int(input())

A = list(map(int, input().split()))
dp = [1] * N

for x in range(1, N):
  for y in range(x):
    if A[x] > A[y]:
      dp[x] = max(dp[x], dp[y]+1)

print(max(dp))