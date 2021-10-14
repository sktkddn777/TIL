def solution(s):
  if len(s) == 4 or len(s) == 6:
    for alp in s:
      if alp.isalpha():
        return False
    return True
  return False