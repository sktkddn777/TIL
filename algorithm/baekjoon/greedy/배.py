import sys

input = sys.stdin.readline
N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

box.sort(reverse=True)
crain.sort(reverse=True)

if box[0] > crain[0]:
  total = -1
else:
  total = 0
  while True:
    if not box:
      break
    for n in range(N):
      for m in range(len(box)):
        if crain[n] >= box[m]:
          box.remove(box[m])
          break
    total += 1

print(total)