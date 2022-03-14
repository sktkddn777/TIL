T = int(input())
for _ in range(T):
  n = int(input())
  arr = []
  for _ in range(2):
    arr.append([0] + list(map(int, input().split())))
  dp = [[0] * (n + 1) for _ in range(2)]
  dp[0][1], dp[1][1] = arr[0][1], arr[1][1]

  for i in range(2, n + 1):
    dp[0][i] = max(dp[1][i-1], dp[1][i-2], dp[0][i-2]) + arr[0][i]
    dp[1][i] = max(dp[0][i-1], dp[1][i-2], dp[0][i-2]) + arr[1][i]
  print(max(max(dp[0]), max(dp[1])))