def solution(s, n):
  answer = ''
  for x in s:
    if x == ' ':
      answer += ' '
    else:
      num = ord(x) + n
      if x.isupper():
        if num > 90:
          answer+= chr(num -26)
        else:
          answer += chr(num)
      else:
        if num > 122:
          answer+= chr(num-26)
        else:
          answer+= chr(num)
  return answer