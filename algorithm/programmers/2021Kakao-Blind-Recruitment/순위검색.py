'''
2021 kakao blind recruitment
programmers coding test practice
'''

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
  res = []
  dic = defaultdict(list)
  for i in info:
    i = i.split()
    condition = i[:-1]
    score = int(i[-1])
    for x in range(5):
      case = list(combinations([0,1,2,3], x))
      for c in case:
        tmp = condition.copy()
        for j in c:
          tmp[j] = '-'
        key = ''.join(tmp)
        dic[key].append(score)
  
  for v in dic.values():
    v.sort()

  for q in query:
    q = (q.replace('and', '')).split()
    target_k = ''.join(q[:-1])
    target_s = int(q[-1])
    count = 0
    if target_k in dic:
      lst = dic[target_k]
      idx = bisect_left(lst, target_s)
      count = len(lst) - idx
    res.append(count)
  return res

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


'''
시간초과 나는 답
'''
# def check_score(n1, n2):
#   if int(n2) >= int(n1):
#     return True
#   return False

# def solution(info, query):
#   user_info = []
#   query_info = []

#   for i in info:
#     user_info.append(i.split())
  
#   for q in query:
#     query_info.append((q.replace('and', '')).split())

#   res = []
#   for q in query_info:
#     num = 0
#     for user in user_info:
#       sub_lst = list(set(q[:-1]) - set(user[:-1]))
#       if len(sub_lst) == 0 or len(sub_lst) == 1 and sub_lst[0] == '-':
#         if check_score(q[-1], user[-1]):
#           num += 1
#     res.append(num)
#   return res