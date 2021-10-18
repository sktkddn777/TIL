'''
점화식이라는 걸 찾는 과정을 못했다.

어떠한 규칙을 찾는 것을 목표로 문제에 접근해야겠다.
'''

def solution(n, money):
    money = sorted(money)
    dp = [[1 if i % money[0] == 0 else 0 for i in range(n+1)]]

    for i in range(len(money)-1):
        dp.append([0] * len(dp[0]))

    for x in range(1, len(money)):
        for y in range(n+1):
            if y < money[x]:
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = dp[x-1][y] + dp[x][y-money[x]]

    return dp[-1][-1] % 1000000007
