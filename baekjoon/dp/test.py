from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

vector = []
for num in A:
  if len(vector) == 0:
    vector.append(num)
    continue
  
  if num > vector[-1]:
    vector.append(num)
  else:
    idx = bisect_left(vector, num)
    vector[idx] = num

print(len(vector))
