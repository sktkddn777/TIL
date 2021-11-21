import heapq
import sys
input= sys.stdin.readline

N = int(input())

class_lst = []
for _ in range(N):
  class_lst.append(list(map(int, input().split())))

class_lst.sort(key=lambda x:x[0])

heap = []
for c in class_lst:
  if heap and c[0] >= heap[0]:
    heapq.heappop(heap)
  heapq.heappush(heap, c[1])

print(len(heap))
