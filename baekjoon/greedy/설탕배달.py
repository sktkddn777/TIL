N = int(input())

answer = 0
five = N // 5
for i in range(five, -1, -1):
  left_N = N - (i * 5)

  if left_N % 3 == 0:
    answer = i + (left_N // 3)
    break

if answer == 0:
  print('-1')
else:
  print(answer)