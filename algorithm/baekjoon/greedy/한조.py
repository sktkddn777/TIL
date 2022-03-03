N = int(input())
peaks = list(map(int, input().split()))

kill = []

total = 0
top = peaks[0]
for i in range(N-1):
  if top > peaks[i+1]:
    total += 1
  else:
    kill.append(total)
    total = 0
    top = peaks[i+1]

kill.append(total)
print(max(kill))