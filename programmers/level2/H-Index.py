def solution(citations):
    citations.sort(reverse=True)
    
    if citations[0] == 0:
        return 0
    for i, citation in enumerate(citations):
        if citation <= i:
            break
        answer = i
    return answer + 1