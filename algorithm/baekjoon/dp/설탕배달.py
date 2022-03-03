N = int(input())

res = -1
five_count = 0

while five_count * 5 <= N:
  temp = N - (5 * five_count)
  if temp % 3 == 0:
    res = five_count + (temp // 3)
  five_count += 1

print(res)