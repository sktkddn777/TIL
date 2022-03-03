import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for op in operations:
        n = op.split()
        try:
            if n[0] == 'I':
                heapq.heappush(min_heap, int(n[1]))
                heapq.heappush(max_heap, -int(n[1]))
            else:
                if n[1] == '-1':
                    res = heapq.heappop(min_heap)
                    max_heap.remove(-res)
                else:
                    res = heapq.heappop(max_heap)
                    min_heap.remove(-res)
        except:
            pass

    if len(min_heap) > 0:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0,0]