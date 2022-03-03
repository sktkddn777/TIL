'''
문제 접근 방법: 값의 차가 가장 최소가 되는 모양은?? 생각해보기
힌트를 보고 알게되었다.
'''

from collections import deque

T = int(input())

for _ in range(T):
  N = int(input())
  log = list(map(int, input().split()))
  log = sorted(log, reverse=True)
  distance = deque()
  for i in range(len(log)):
    if i % 2 == 1:
      distance.append(log[i])
    else:
      distance.appendleft(log[i])
  
  res = 0
  for i in range(len(distance)-1):
    if res < abs(distance[i+1] - distance[i]):
      res = abs(distance[i+1] - distance[i])
  print(res)