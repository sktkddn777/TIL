N = int(input())
distance = list(map(int, input().split()))
oil_lst = list(map(int, input().split()))

min_oil = oil_lst[0]
total = 0

for i in range(len(oil_lst)-1):
  if oil_lst[i] <= min_oil:
    min_oil = oil_lst[i]
  total += distance[i] * min_oil

print(total)