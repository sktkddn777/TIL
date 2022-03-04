T = int(input())
arr_zero = [0] * 41
arr_one = [0] * 41
arr_zero[0], arr_zero[1] = 1, 0
arr_one[0], arr_one[1] = 0, 1
for _ in range(T):
  N = int(input())
  i = 2
  while i <= N:
    arr_zero[i] = arr_zero[i - 1] + arr_zero[i - 2]
    arr_one[i] = arr_one[i - 1] + arr_one[i - 2]
    i += 1
  print(arr_zero[N], arr_one[N])