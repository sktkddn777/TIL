# KMP 이해 X

# S = list(input())
# P = list(input())

# def KMP_table(word):
#     table = [0] * len(word)

#     j = 0
#     for i in range(1, len(word)):
#         while j > 0 and word[i] != word[j]:
#             j = table[j-1]
#         if word[i] == word[j]:
#             j += 1
#             table[i] = j
#     return table

# def KMP(S, P):
#     n, m = len(S), len(P)
#     table = KMP_table(S)
#     idx = 0

#     for i in range(n):
#         while idx > 0 and S[i] != P[idx]:
#             idx = table[idx-1]
#         if S[i] == P[idx]:
#             if idx == m-1:
#                 return 1
#             else:
#                 idx += 1
#     return 0

# print(KMP(S, P))