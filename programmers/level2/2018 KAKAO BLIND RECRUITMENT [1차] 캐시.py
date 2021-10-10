from collections import deque


def solution(cacheSize, cities):
    answer = 0

    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.upper()
        if len(cache) < cacheSize:
            if city in cache:
                cache.remove(city)
                answer += 1
            else:
                answer += 5
            cache.appendleft(city)
        else:
            if city in cache:
                cache.remove(city)
                answer += 1
            else:
                cache.pop()
                answer += 5
            cache.appendleft(city)

    return answer
