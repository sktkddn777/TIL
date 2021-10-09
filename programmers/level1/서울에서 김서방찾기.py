def solution(seoul):
    for i, s in enumerate(seoul):
        if s == 'Kim':
            answer = i
            break


    return f'김서방은 {answer}에 있다'