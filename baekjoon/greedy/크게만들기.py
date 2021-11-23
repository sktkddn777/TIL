N, K = map(int, input().split())

num = list(input())
stack = [num[0]]

idx = 1
while K > 0 and idx < len(num):
  if int(num[idx]) <= int(stack[-1]):
    stack.append(num[idx])
  else:
    while int(stack[-1]) < int(num[idx]):
      stack.pop()
      K -= 1
      if K == 0:
        break
      if not stack:
        break
    stack.append(num[idx])
  idx += 1

if K > 0:
  stack = ''.join(stack)
  print(stack[:-K])
else:
  stack += num[idx:]
  stack = ''.join(stack)
  print(stack)