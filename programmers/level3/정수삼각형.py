def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        for x in range(1, len(triangle[i])-1):
            triangle[i][x] = triangle[i][x] + max(triangle[i-1][x-1], triangle[i-1][x])
        triangle[i][-1] += triangle[i-1][-1]

    return max(triangle[-1])