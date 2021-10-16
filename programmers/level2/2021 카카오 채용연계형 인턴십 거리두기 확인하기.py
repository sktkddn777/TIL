def distance(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(5):
        for y in range(5):
            if arr[x][y] == 'P':
                for i in range(4):
                    tx = x + dx[i]
                    ty = y + dy[i]

                    if 0 <= tx < 5 and 0 <= ty < 5:
                        if arr[tx][ty] == 'P':
                            return 0
                        else:
                            arr[tx][ty] -= 1

    for x in arr:
        for y in x:
            if y != 'P':
                if y <= -2:
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        for a in range(5):
            place[a] = list(place[a])
            for b in range(5):
                if place[a][b] == 'X':
                    place[a][b] = 10
                elif place[a][b] == 'O':
                    place[a][b] = 0
        answer.append(distance(place))
    return answer