square_num = [x*x for x in range(1, 317)]
N = int(input())
dp = [0] * (N+1)

for i in range(1, N+1):
  num = float('inf')
  for y in square_num:
    if y > i:
      break
    num = min(num, dp[i - y]+1)
  dp[i] = num

print(dp[N])