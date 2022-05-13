N = int(input())
lst = list(map(int, input().split()))
res = [0] * N
stack = [(lst[N-1], N-1)]

for i in range(N-2, -1, -1):
    while lst[i] > stack[-1][0]:
        res[stack[-1][1]] = i+1
        stack.pop()
        if not stack:
            break

    stack.append((lst[i], i))

for x in stack:
    res[x[1]] = 0

print(*res)
