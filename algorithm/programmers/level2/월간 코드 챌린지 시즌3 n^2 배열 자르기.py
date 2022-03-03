'''
끝까지 풀라했는데 시간초과걸리고
안풀리다가 구글에 답을 찾았다...

'''

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        
        if a < b:
            a,b = b,a
        answer.append(a + 1)
    return answer