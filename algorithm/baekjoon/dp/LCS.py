arr = []
for _ in range(2):
  arr.append(input())

N, M = len(arr[0]), len(arr[1])
ans = [0] * N

for i in range(M):
  cnt = 0
  for j in range(N):
    if ans[j] > cnt:
      cnt = ans[j]
    elif arr[0][j] == arr[1][i]:
      ans[j] = cnt + 1
print(max(ans))