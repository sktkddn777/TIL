N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if lst[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i + lst[i][0]] + lst[i][1], dp[i+1])

print(dp[0])