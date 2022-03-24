from collections import deque
def solution(numbers, target):
    queue = deque([])

    for num in numbers:
      if queue:
        N = len(queue)
        for i in range(N):
          x = queue.popleft()
          queue.append(x + num)
          queue.append(x - num)
      else:
        queue.append(num)
        queue.append(-num)

    return queue.count(target)