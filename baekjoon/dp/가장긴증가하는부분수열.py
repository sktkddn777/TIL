# DP를 이용하는 방법

# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# dp = [1] * N

# for i in range(1, N):
#   for j in range(i):
#     if A[i] > A[j]:
#       dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

# 이분 탐색을 이용하는 방법

import sys 
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

vector = []

for i in range(N):
  if not vector:
    vector.append(A[i])
    continue

  if vector[-1] < A[i]:
    vector.append(A[i])
  else:
    index = bisect_left(vector, A[i])
    vector[index] = A[i]

print(len(vector))