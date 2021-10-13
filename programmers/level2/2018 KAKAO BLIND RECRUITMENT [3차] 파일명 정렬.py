'''
set 으로 정렬하는 법 (lambda사용)
'''

def solution(files):
    answer = []
    res = []
    for file in files:
        head, number, tail = '', '', ''
        num_appear = True

        for i in range(len(file)):
            if num_appear:
                head += file[i]
                if file[i+1].isdigit():
                    num_appear = False
            else:
                if file[i].isdigit():
                    num_appear = False
                    number += file[i]
                else:
                    tail = file[i:]
                    break
        answer.append((head, number, tail))

    answer.sort(key=lambda x:(x[0].lower(),int(x[1])))

    for x in answer:
        res.append(''.join(x))
    return res