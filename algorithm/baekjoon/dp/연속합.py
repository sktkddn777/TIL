n = int(input())

num_lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = num_lst[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + num_lst[i], num_lst[i])

print(max(dp))