from collections import defaultdict
import heapq

def max_heap(lst):
  heap = []
  for x in lst:
    heapq.heappush(heap, (-x[0], x[1]))
  return heap

def solution(genres, plays):
  answer = []
  genre_dic = defaultdict(list)
  for i in range(len(genres)):
    genre_dic[genres[i]].append((plays[i], i))

  sum_dic = defaultdict(int)
  for k in genre_dic:
    sum_dic[k] = sum(x[0] for x in genre_dic[k])

  sorted_sum = sorted(sum_dic.items(), key=lambda x: x[1], reverse=True)
  for k in sorted_sum:
    tmp_h = max_heap(genre_dic[k[0]])
    if len(genre_dic[k[0]]) < 2:
      answer.append(heapq.heappop(tmp_h)[1])
    else:
      for _ in range(2):
        answer.append(heapq.heappop(tmp_h)[1])

  return answer