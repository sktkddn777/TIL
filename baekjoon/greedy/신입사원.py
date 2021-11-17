import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  volunteer_lst = []
  success = [0] * N

  for _ in range(N):
    volunteer_lst.append(list(map(int, input().split())))
  
  volunteer_lst = sorted(volunteer_lst, key=lambda x:x[0])

  total = 1
  rank_second = volunteer_lst[0][1]
  for i in range(1, len(volunteer_lst)):
    if volunteer_lst[i][1] < rank_second:
      rank_second = volunteer_lst[i][1]
      total += 1

  print(total)

    