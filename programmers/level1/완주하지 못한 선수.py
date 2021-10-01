def solution(participant, completion):
    dict = {}
    for name in participant:
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1
    
    for name in completion:
        if name in dict:
            dict[name] -= 1
    
    for key in dict.keys():
        if dict[key] == 1:
            answer = key
            
    return answer