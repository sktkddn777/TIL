S = int(input())

num = 1
while True:
  if num*(num+1) // 2 > S:
    break
  num += 1

print(num - 1)