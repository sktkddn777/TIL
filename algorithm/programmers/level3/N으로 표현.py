'''
구글을 통해서 힌트를 얻었다.

'''

def calculate(lst1, lst2):
    lst = []
    for x in lst1:
        for y in lst2:
            lst.extend([x+y, x-y, x*y])
            if y != 0:
                lst.extend([x//y])

    return list(set(lst))

def solution(N, number):
    dp = [[N]]
    connect = str(N)
    while True:
        if number in dp[-1]:
            return len(dp)

        if len(dp) > 8:
            return -1

        connect += str(N)
        lst = [int(connect)]
        for i in range(len(dp)):
            lst.extend(calculate(dp[i], dp[len(dp) - (i+1)]))

        dp.append(list(set(lst)))