def solution(dirs):
    visited = []
    x, y = 5, 5

    for d in dirs:
        dx, dy = x, y

        if d == 'U':
            y += 1
        elif d == 'D':
            y -= 1
        elif d == 'R':
            x += 1
        elif d == 'L':
            x -= 1

        if 0<= x <= 10 and 0<= y <= 10:
            visited.append((x,y,dx,dy))
            visited.append((dx,dy,x,y))
        else:
            x, y = dx, dy

    answer = len(set(visited)) // 2

    return answer