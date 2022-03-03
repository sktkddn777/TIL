'''
오랜만에 DP로 풀었다.
방법을 처음에는 못찾아서 구글링을 했다.
다행히 DP를 쓰는 방법은 금방 익혔다.
'''

def solution(board):
    answer = 0
    sero = len(board)
    garo = len(board[0])

    for s in range(1, sero):
      for g in range(1, garo):
        if board[s][g] == 1:
          board[s][g] += min(board[s-1][g-1], board[s-1][g], board[s][g-1])

    for i in range(sero):
      if answer < max(board[i]):
        answer = max(board[i])

    return answer ** 2