def solution(s):
    answer = ''
    boolean = True
    for word in s:
        if boolean:
            word = word.upper()
            boolean = False
        else:
            word = word.lower()

        if word == ' ':
            boolean = True
        answer += word
    return answer