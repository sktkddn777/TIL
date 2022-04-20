N, K = map(int, input().split())

n = 0
while K > 0 and n <= N:
    n += 1
    if N % n == 0:
        K -= 1

if K > 0:
    print(0)
else:
    print(n)
