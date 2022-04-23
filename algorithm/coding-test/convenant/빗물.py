H, W = map(int, input().split())
block_lst = list(map(int, input().split()))

N = len(block_lst) - 1

l_idx, r_idx = 0, N
l_max, r_max = block_lst[0], block_lst[N] 
res = 0

while l_idx != r_idx:
    if l_max > r_max:
        r_idx -= 1
        if block_lst[r_idx] < r_max:
            res += (r_max - block_lst[r_idx])
        else:
            r_max = block_lst[r_idx]
    else:
        l_idx += 1
        if block_lst[l_idx] < l_max:
            res += (l_max - block_lst[l_idx])
        else:
            l_max = block_lst[l_idx]

print(res)



# 기존 풀이

# H, W = map(int, input().split())

# lst = [[0] * W for _ in range(H)]
# block_lst = list(map(int, input().split()))

# for i in range(W):
#     for j in range(block_lst[i]):
#         lst[H-1-j][i] = 1


# res = 0
# for i in range(H):
#     tmp = 0
#     flg = 0
#     for j in range(W):
#         if not flg and lst[i][j] == 1:
#             flg = 1
#         elif flg and lst[i][j] == 0:
#             tmp += 1
#         elif flg and lst[i][j] == 1 and tmp != 0:
#             res += tmp
#             tmp = 0

# print(res)