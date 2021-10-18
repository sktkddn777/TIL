'''

'''

def solution(n):
    answer = []

    def move(s, e):
        answer.append([s,e])

    def hanoi(disk, start, end, via):
        if disk == 1:
            move(start, end)
        else:
            hanoi(disk-1, start, via, end)
            move(start, end)
            hanoi(disk-1, via, end, start)

    hanoi(n, 1, 3, 2)

    return answer