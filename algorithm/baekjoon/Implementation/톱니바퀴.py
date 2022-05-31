from collections import deque

gear_lst = []
for _ in range(4):
    gear_lst.append(deque(list(input())))

K = int(input())
turn_lst = []
for _ in range(K):
    turn_lst.append(list(map(int, input().split())))

def do_rotate(idx, dir):
    if dir == 1:
        gear_lst[idx].appendleft(gear_lst[idx].pop())
    else:
        gear_lst[idx].append(gear_lst[idx].popleft())

def check(start, dir):
    rotate = [0 for _ in range(4)]
    rotate[start] = 1
    
    # check left
    for i in range(start-1, -1, -1):
        if gear_lst[i][2] != gear_lst[i+1][6]:
            rotate[i] = 1
        else:
            break
    
    # check right
    for i in range(start+1, 4):
        if gear_lst[i-1][2] != gear_lst[i][6]:
            rotate[i] = 1
        else:
            break

    for i in range(4):
        if rotate[i] and (start-i) % 2 == 0:
            do_rotate(i, dir)
        elif rotate[i] and (start-i) % 2 == 1:
            do_rotate(i, dir * (-1))


for turn, direction in turn_lst:
    check(turn-1, direction)

res = 0
for i in range(4):
    res += (int(gear_lst[i][0]) * (2**i))

print(res)
    