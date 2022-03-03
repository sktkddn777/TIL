'''
뭔소린지 모르겠어서 구글링 했다.
다음에 풀 때는 혼자 해보자.

'''
def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def quad_tree(x, y, N):
        num = arr[x][y]

        for i in range(x, x + N):
            for z in range(y, y + N):
                if arr[i][z] != num:
                    n = N // 2
                    quad_tree(x, y, n)
                    quad_tree(x, y+n, n)
                    quad_tree(x+n, y, n)
                    quad_tree(x+n, y+n, n)
                    return
        answer[num] += 1
    quad_tree(0, 0, length)
    return answer