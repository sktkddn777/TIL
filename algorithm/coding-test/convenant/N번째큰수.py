N = int(input())

for _ in range(N):
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[7])