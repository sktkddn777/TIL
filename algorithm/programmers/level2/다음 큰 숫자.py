def solution(s):
    left = 0
    right = 0

    for i in s:
      if i == '(':
        left += 1
      else:
        right += 1

      if right > left:
        return False

    if right != left:
      return False
    return True