import heapq
import sys
input = sys.stdin.readline
N = int(input())
queue1 = []
queue2 = []

for i in range(N):
  n = int(input())
  if len(queue1) == len(queue2):
    heapq.heappush(queue1, -n)
  else:
    heapq.heappush(queue2, n)

  if queue1 and queue2:
    if -queue1[0] > queue2[0]:
      a = heapq.heappop(queue1)
      b = heapq.heappop(queue2)
      heapq.heappush(queue2, -a)
      heapq.heappush(queue1, -b)
  print(-queue1[0])
  