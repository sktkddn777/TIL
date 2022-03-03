from collections import deque

def solution(numbers, target):
    ans = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        data = queue.popleft()
        if data[0] < len(numbers):
            queue.append([data[0] + 1, data[1] + numbers[data[0]]])
            queue.append([data[0] + 1, data[1] - numbers[data[0]]])
        else:
            if data[1] == target:
                ans += 1
    return ans