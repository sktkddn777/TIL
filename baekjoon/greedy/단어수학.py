'''
계속 틀려서 검색을 해봤다.


모든 숫자의 자릿수 합을 먼저 구하고
그 자릿수에 따라 정렬!! 그리고 그리디.

'''

from collections import defaultdict

N = int(input())
word_lst = []
word_weight = defaultdict(list)

for _ in range(N):
  word_lst.append(input())

for word in word_lst:
  idx = len(word) - 1

  for w in word:
    if w not in word_weight:
      word_weight[w] = 10 ** idx
    else:
      word_weight[w] += 10 ** idx
    idx -= 1

word_weight = sorted(word_weight.values(), reverse=True)

num = 9
total = 0
for weight in word_weight:
  total += (num * weight)
  num -= 1

print(total)