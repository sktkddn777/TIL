from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    sum_truck = 0
    while len(bridge):
        answer += 1
        sum_truck -= bridge[0]
        bridge.popleft()
        if truck_weights:
            if sum_truck + truck_weights[0] <= weight:
                sum_truck += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer