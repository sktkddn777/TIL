def fibo(n):
    dp = [0] * (n+1)
    if n == 0:
        return 0
    if n < 3:
        return 1
    
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return (dp[-1])

N = int(input())
print(fibo(N))