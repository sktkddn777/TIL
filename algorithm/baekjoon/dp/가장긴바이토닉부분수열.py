
n = int(input())
arr = list(map(int, input().split()))
arr_rev = list(reversed(arr))

dp1 = [1] * n
dp2 = [1] * n

for i in range(1, n):
  for j in range(i):
    if arr[i] > arr[j]:
      dp1[i] = max(dp1[i], dp1[j] + 1)
    if arr_rev[i] > arr_rev[j]:
      dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = dp2[::-1]
ans = 0
for i in range(n):
  if dp1[i] + dp2[i] - 1 > ans:
    ans = dp1[i] + dp2[i] - 1

print(ans)