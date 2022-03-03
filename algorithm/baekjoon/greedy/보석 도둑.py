'''
검색했음
'''
'''
heapq를 사용하는 문제인걸 캐치해야한다.
(우선순위큐) 
가격에 관해서 우선순위큐로 해줘야 하고, 그에 따른 조건으로는 무게를 고려해야 한다.

결국에는 검색을 통해서 답을 구했지만 다음에는 혼자서 풀어볼 수 있도록!!
'''

import sys
import heapq

input = sys.stdin.readline
N, K = map(int,input().split())

jewl_lst = []
bag_lst = []
for _ in range(N):
  heapq.heappush(jewl_lst, list(map(int, input().split())))

for _ in range(K):
  bag_lst.append(int(input()))

jewl_lst.sort()
bag_lst.sort()

heap = []
total = 0
for bag in bag_lst:
  while jewl_lst and jewl_lst[0][0] <= bag:
    heapq.heappush(heap, -jewl_lst[0][1])
    heapq.heappop(jewl_lst)
  
  if heap:
    total += heapq.heappop(heap)
  elif not jewl_lst:
    break

print(-total)
  
