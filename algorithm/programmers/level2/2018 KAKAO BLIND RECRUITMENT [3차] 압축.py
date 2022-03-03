def solution(msg):
    answer = []
    lzw_dic = {}

    for alp in range(1, 27):
        lzw_dic[chr(alp+64)] = alp
    last_num = 27
    index = len(msg)
    while msg:
        if msg[:index] in lzw_dic:
            answer.append(lzw_dic[msg[:index]])
            if index != len(msg):
                lzw_dic[msg[:index]+msg[index]] = last_num
                last_num += 1
                msg = msg[index:]
                index = len(msg)
            else:
                break
        else:
            index -= 1

    return answer
