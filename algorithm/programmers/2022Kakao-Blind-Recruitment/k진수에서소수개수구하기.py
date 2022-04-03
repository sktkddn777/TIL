'''
2022 kakao blind recruitment
programmers coding test practice
'''
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def convert_base(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return (rev_base[::-1])

def solution(n, k):
    k_base = convert_base(n, k)
    j = 0
    ans = 0
    for i in range(len(k_base)):
        if k_base[i] == '0':
            if i != j:
                if is_prime(int(k_base[j:i])):
                    ans += 1
                j = i + 1

    if is_prime(int(k_base[j:i+1])):
        ans += 1
    
    return ans

solution(110011, 10)