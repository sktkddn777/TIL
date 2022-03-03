# https://mjmjmj98.tistory.com/150
'''
완전 탐색을 사용하는 방법을 생각했다.
회전에 대한 공식도 찾았다.

다만 이런 복잡한 문제는 처음봐서... 내 방법이 맞는지 확신이 안들어 블로그를 참조했다.

리스트를 확장하는 방법을 쓰는 점에서 새로운 문제풀이를 알게 되었다.


'''

def rotate(lst):
    M = len(lst)
    result = [[0] * M for _ in range(M)]

    for x in range(M):
        for y in range(M):
            result[y][M-1-x] = lst[x][y]
    return result


def check(lock_lst):
    n = len(lock_lst) // 3

    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock_lst[i][j] != 1:
                return False
    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)

    lock_location = [[0] * (N*3) for _ in range(N*3)]

    for x in range(N):
        for y in range(N):
            lock_location[x+N][y+N] = lock[x][y]

    for i in range(N*2):
        for j in range(N*2):
            # 회전
            temp_lst = key
            for _ in range(4):
                temp_lst = rotate(temp_lst)

                for x in range(M):
                    for y in range(M):
                        lock_location[i+x][j+y] += temp_lst[x][y]

                if check(lock_location):
                    return True

                for x in range(M):
                    for y in range(M):
                        lock_location[i+x][j+y] -= temp_lst[x][y]
    return False