'''
2021 kakao blind recruitment
programmers coding test practice
'''

def upper_to_lower(id):
  return id.lower()

def preprocess(id):
  symbol = ['-', '_', '.']
  res = ''
  for x in id:
    if 'a' <= x <= 'z' or x.isdigit() or x in symbol:
      res += x
  return res

def punctuation(id):
  res = ''
  flag = 0
  for x in id:
    if flag and x == '.':
      continue
    if x == '.':
      flag = 1
    else:
      flag = 0
    res += x
  return res

def punctuation_remove(id):
  front, back = 0, len(id)
  if id[0] == '.':
    front += 1
  if id[-1] == '.':
    back -= 1
  return id[front:back]

def check_null(id):
  if len(id) == 0:
    return ('a')
  return (id)

def check_length(id):
  if len(id) >= 16:
    id = id[:15]
  return punctuation_remove(id)

def length_up(id):
  if len(id) <= 2:
    while len(id) < 3:
      id += id[-1]
  return id

def solution(new_id):
  # new_id -> string
  new_id = upper_to_lower(new_id)
  new_id = preprocess(new_id)
  new_id = punctuation(new_id)
  new_id = punctuation_remove(new_id)
  new_id = check_null(new_id)
  new_id = check_length(new_id)
  new_id = length_up(new_id)

  return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))