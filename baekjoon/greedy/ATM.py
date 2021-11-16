N = int(input())
lst = list(map(int, input().split()))

lst = sorted(lst, reverse=True)

total = 0
for i in range(N):
  total += sum(lst[i:])

print(total)