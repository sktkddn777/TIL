def solution(n, a, b):
    answer = 1
    if a>b:
        a, b = b, a
        
    if a%2 != 0:
        if abs(a-b) == 1:
            return answer
        
    while True:
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1

        a = a // 2
        b = b // 2
        answer += 1

        if a % 2 != 0:
            if abs(a - b) == 1:
                return answer