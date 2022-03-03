def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    
    a = 0
    for i in range(len(B)):
        if B[i] > A[a]:
            answer += 1
            a += 1
            
    return answer