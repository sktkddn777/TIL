def solution(price, money, count):
    total = 0
    for c in range(1, count+1):
        total += (price * c)
    if total <= money:
        return 0
    return total - money

print(solution(3, 20, 4))