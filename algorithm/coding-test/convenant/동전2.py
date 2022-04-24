n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for c in coin:
    for j in range(c, k+1):
        if j >= c:
            dp[j] = min(dp[j], dp[j-c]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])