'''
2021 kakao blind recruitment
programmers coding test practice
'''

from itertools import combinations
from collections import Counter

def choice(orders, c_len):
  candidate_lst = []

  for x in orders:
    candidate_lst += combinations(sorted(x), c_len)

  res = Counter(candidate_lst).most_common()
  return [''.join(x) for x, v in res if v > 1 and v == res[0][1]]

def solution(orders, course):
  res = []
  for c in course:
    res += choice(orders, c)
      
  res.sort()
  return res

print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))