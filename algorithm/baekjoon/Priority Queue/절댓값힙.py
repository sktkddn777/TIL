import heapq
import sys

input = sys.stdin.readline
N = int(input())
queue = []
for _ in range(N):
  n = int(input())
  if n == 0:
    if len(queue) == 0:
      print(0)
    else:
      print(heapq.heappop(queue)[1])
  else:
    heapq.heappush(queue, (abs(n), n))
