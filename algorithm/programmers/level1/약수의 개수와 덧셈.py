def is_yaksu(num):
  count = 0
  for i in range(1, num+1):
    if num % i == 0:
      count += 1
  
  if count %2 == 0:
    return True
  return False

def solution(left, right):
    answer = 0
    num_lst = [x for x in range(left, right+1)]

    for num in num_lst:
      if is_yaksu(num):
        answer += num
      else:
        answer -= num
    return answer