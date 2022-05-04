'''
sangwoo 2022-05-04

시간제한이 0.5로 굉장히 짧다.
sum 내장함수를 사용하면 시간 초과가 난다.
while + sum -> O(N^2)
'''
def solution():
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))

    start, end = 0, 1
    tmp_sum = lst[0]
    res = 100001

    while end <= N:
        if tmp_sum >= S:
            res = min(res, end-start)
            tmp_sum -= lst[start]
            start += 1
        else:
            if end == N:
                break
            tmp_sum += lst[end]
            end += 1

    return res % 100001

if __name__ == '__main__':
    res = solution()
    print(res)