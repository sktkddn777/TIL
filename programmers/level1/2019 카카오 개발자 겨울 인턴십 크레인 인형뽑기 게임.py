def solution(board, moves):
    answer = 0
    bucket =[]
    stack = 0

    for i in range(len(moves)):
        for y in range(len(board)):
            if board[y][moves[i] - 1] == 0:
                continue
            else:
                bucket.append(board[y][moves[i] - 1])
                board[y][moves[i] - 1] = 0
                stack += 1
                if stack > 1:
                    if bucket[stack - 1] == bucket[stack - 2]:
                        del(bucket[-2:])
                        answer += 2
                        stack -= 2
                break
    return answer