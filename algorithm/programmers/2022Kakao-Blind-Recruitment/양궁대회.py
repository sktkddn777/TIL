from collections import deque

def bfs(n, info):
  queue = deque([(0, [0] * 11)])
  max_num = 0
  ans = []

  while queue:
    cur, arrow = queue.popleft()
    if sum(arrow) == n:
      lion, appeach = 0, 0
      for i in range(10):
        if not info[i] == arrow[i] == 0:
          if info[i] >= arrow[i]:
            appeach += (10 - i)
          else:
            lion += (10 - i)
      if (lion - appeach) >= max_num:
        ans = arrow
        max_num = lion - appeach
    else:
      if sum(arrow) > n:
        continue
      
      elif cur == 10:
        tmp = arrow.copy()
        tmp[cur] = n - sum(tmp)
        queue.append((-1, tmp))

      else:
        tmp = arrow.copy()
        tmp[cur] = 0
        queue.append((cur+1, tmp))
        tmp = arrow.copy()
        tmp[cur] = info[cur] + 1
        queue.append((cur+1, tmp))
  if 0 == max_num:
    return []
  return ans

def solution(n, info):
    answer = bfs(n, info)
    if answer == []:
      return [-1]
    return answer

print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))