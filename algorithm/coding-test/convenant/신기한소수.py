import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def dfs(num, N):
    if len(str(num)) == N:
        print(num)
    else:
        for x in [1, 3, 7, 9]:
            if is_prime(num * 10 + x):
                dfs(num * 10 + x, N)

if __name__ == '__main__':
    N = int(input())

    for x in [2, 3, 5, 7]:
        dfs(x, N)

'''
에라토스테네스의 체를 쓰면 메모리 초과가 난다.
시간초과도 발생한다.

다른 방법.
'''