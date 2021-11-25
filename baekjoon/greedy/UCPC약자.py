from collections import deque
string = input()

ucpc = deque(['U', 'C', 'P','C'])
for s in string:
  if ucpc:
    if s == ucpc[0]:
      ucpc.popleft()
  else:
    break

if len(ucpc) == 0:
  print("I love UCPC")
else:
  print("I hate UCPC")