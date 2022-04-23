N, S = map(int, input().split())
num_lst = list(map(int, input().split()))

res = 100000
left, right = 0, 0
sum = 0

while right <= N:
    if sum < S:
        if right == N:
            break
        sum += num_lst[right]
        right += 1
    else:
        if left >= right:
            break
        res = min(res, right - left)
        sum -= num_lst[left]
        left += 1


if res == 100000:
    print(0)
else:
    print(res)





# 시간초과 코드
# import sys

# input = sys.stdin.readline
# N, S = map(int, input().split())
# num_lst = list(map(int, input().split()))

# left, right = 0, len(num_lst)
# if sum(num_lst) < S:
#     print(0)
# else:
#     while True:
#         if num_lst[left] > num_lst[right-1]:
#             right -= 1
#         else:
#             left += 1
        
#         if sum(num_lst[left: right]) < S:
#             print(right - left + 1)
#             break