from itertools import combinations


antic = {'a', 'n', 't', 'i', 'c'}

alpha = {ky: v for v, ky in enumerate(
    set(map(chr, range(ord('a'), ord('z') + 1))) - antic
)}

def word_to_bin(word):
    ans = 0b0
    for w in word:
        ans = ans | (1 << alpha[w])
    return ans

N, K = map(int, input().split())
if K < 5:
    print(0)
else:
    w_lst = []
    for _ in range(N):
        w_lst.append(set(input()) - antic)

    bin_lst = [word_to_bin(x) for x in w_lst]
    res = 0
    power_2 = [2 ** i for i in range(21)]
    for comb in combinations(power_2, K-5):
        cur = sum(comb)
        cnt = 0
        for bin in bin_lst:
            if bin & cur == bin:
                cnt += 1
        res = max(res, cnt)

print(res)
# 시간초과 기존 풀이 (백트랙킹)
# N, K = map(int, input().split())
# alp_lst = [0] * 26
# alp_lst[0], alp_lst[2], alp_lst[8], alp_lst[13], alp_lst[19] = 1, 1, 1, 1, 1

# res = []
# word_lst = []
# for _ in range(N):
#     word_lst.append(list(ord(x)-97 for x in list(input()))[4:-4])

# def dfs(n):
#     global res
#     if n == 0:
#         cnt = 0
#         for word in word_lst:
#             flg = 1
#             for i in word:
#                 if alp_lst[i] == 0:
#                     flg = 0
#             if flg:
#                 cnt += 1
#         res.append(cnt)
#     else:
#         for i in range(26):
#             if alp_lst[i] == 0:
#                 alp_lst[i] = 1
#                 dfs(n-1)
#                 alp_lst[i] = 0  

# if K <5:
#     print(0)
# else:
#     dfs(K-5)
#     print(max(res))