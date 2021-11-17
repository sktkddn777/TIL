'''
문제를 잘못이해해서 잠깐 해맸다.
heapq는 알고있던 알고리즘이여서 쉽게 풀 수 있었다.
'''

import heapq

N = int(input())
heap = []
for _ in range(N):
  heapq.heappush(heap, int(input()))

total = 0
while len(heap) > 1:
  x1, x2 = heapq.heappop(heap), heapq.heappop(heap)
  total += (x1 + x2)
  heapq.heappush(heap, x1+x2)

print(total)