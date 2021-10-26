def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if a != answer[-1]:
            answer.append(a)
    return answer