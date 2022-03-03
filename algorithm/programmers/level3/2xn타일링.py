def solution(n):
  lst = [0] * 60001
  lst[1], lst[2] = 1, 2

  for i in range(3, n+1):
    lst[i] = (lst[i-1] + lst[i-2]) % 1000000007

  return lst[n]