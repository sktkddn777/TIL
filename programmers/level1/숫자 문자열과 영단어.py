def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2',
           'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    key_list = dic.keys()

    for i in key_list:
        if i in s:
            s = s.replace(i, dic[i])
    
    return int(s)


#s = input()
#print(solution(s))