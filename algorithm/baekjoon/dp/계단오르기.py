N = int(input())
stairs = []
dp = [0] * N

for _ in range(N):
  stairs.append(int(input()))

if N == 1:
  print(stairs[0])
elif N == 2:
  print(stairs[0] + stairs[1])

if N > 2:
  dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]
  dp[2] = stairs[2] + max(stairs[0], stairs[1])
  for i in range(3, N):
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
  print(dp[N-1])