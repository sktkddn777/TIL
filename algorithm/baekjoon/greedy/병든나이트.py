N, M = map(int, input().split())

if N == 1 or M == 1:
  res = 1

elif N == 2:
  res = min(4, ((M-1) // 2)+1)

else:
  if M <= 6:
    res = min(4, M)
  else:
    res = M - 2

print(res)