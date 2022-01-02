T = int(input())

fibo = [(0,0)] * 41
fibo[0] = (1, 0)
fibo[1] = (0, 1)

for i in range(2, 41):
  fibo[i] = [x + y for x, y in zip(fibo[i-1], fibo[i-2])]


for _ in range(T):
  N = int(input())
  print(fibo[N][0], fibo[N][1])
