N = int(input())
score_lst = []

for _ in range(N):
  score_lst.append(int(input()))

score_lst = score_lst[::-1]

total = 0
for i in range(len(score_lst)-1):
  if score_lst[i] <= score_lst[i+1]:
    total += score_lst[i+1] - score_lst[i] + 1
    score_lst[i+1] = score_lst[i]-1

print(total)