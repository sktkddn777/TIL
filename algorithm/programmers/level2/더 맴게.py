import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        mix = num1 + (num2*2)
        heapq.heappush(scoville, mix)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer