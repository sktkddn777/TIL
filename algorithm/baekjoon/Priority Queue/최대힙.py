import heapq
import sys

input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
  n = int(input())
  if n == 0:
    if len(heap) > 0:
      print(-1 * heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, (-n))
