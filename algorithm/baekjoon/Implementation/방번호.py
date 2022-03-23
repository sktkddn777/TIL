import math

N = input()
arr = [0] * 9

six_nine = 0
for n in N:
  if n == '6' or n == '9':
    six_nine += 1
  else:
    arr[int(n)] += 1
print(max(max(arr), math.ceil(six_nine / 2)))