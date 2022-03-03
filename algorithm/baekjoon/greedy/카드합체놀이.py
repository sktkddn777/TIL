import heapq

n, m = map(int, input().split())
card_lst = list(map(int, input().split()))

heap = []
for card in card_lst:
  heapq.heappush(heap, card)

for i in range(m):
  x = heapq.heappop(heap)
  y = heapq.heappop(heap)
  heapq.heappush(heap, x+y)
  heapq.heappush(heap, x+y)

print(sum(heap))

