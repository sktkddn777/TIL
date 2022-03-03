import math

def solution(n):
  num = math.sqrt(n)
  int_num = int(num)
  if num == int_num:
    return (num+1) ** 2
  return -1