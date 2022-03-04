N = int(input())

ans = 0
while True:
  if N < 0:
    ans = -1
    break
  if N % 5 == 0:
    ans += N // 5
    break
  N -= 3
  ans += 1

print(ans)