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

'''
다시 간단하게 푸는 법을 생각해보니까 코드 길이가 엄청 줄었다.
N, K = map(int, input().split())
number = input()
stack = []

for i in range(len(number)):
    while stack and stack[-1] < number[i] and K > 0:
        stack.pop()
        K -= 1

    stack.append(number[i])

if K > 0:
    stack = stack[:-K]
print(''.join(stack))
'''