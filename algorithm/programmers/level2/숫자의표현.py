def solution(n):
    answer = 0

    for i in range(1, n//2 + 1):
        middle = i
        for x in range(i+1, n):
            middle += x
            if middle > n:
                break
            elif middle == n:
                answer += 1
                break
    answer += 1
    return answer
