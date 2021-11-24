'''
문제 이해하는데 어려워서 질문 검색으로 알았다
두 센서간 거리가 긴거 부터 제거하고
남은 거리들의 합으로 구할 수 있는 쉬운 문제

개수 10000 개 O(nlogn)가능.

'''

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

distance = []
for i in range(len(sensor)-1):
  distance.append(sensor[i+1] - sensor[i])

distance = sorted(distance, reverse=True)
print(sum(distance[K-1:]))