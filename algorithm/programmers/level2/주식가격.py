from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        count = 0
        num = prices.popleft()
        for price in prices:
            if price < num:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer