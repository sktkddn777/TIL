'''
처음에는 제귀로 접근했다가 런타임 에러와 시간초과가 떠서 
반복문으로 방법을 바꿨다.
def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    answer = (solution(n-1) + solution(n-2)) % 1234567

    return answer
'''

def solution(n):
    fibo = [0, 1, 1]

    for i in range(3, n+1):
        fibo.append((fibo[i-2] + fibo[i-1])%1234567)
    answer = fibo[-1]
    return answer