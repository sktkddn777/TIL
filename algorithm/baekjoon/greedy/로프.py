N = int(input())

rope_lst = []
for _ in range(N):
  rope_lst.append(int(input()))

rope_lst = sorted(rope_lst, reverse=True)

total = 0

idx = 1
for rope in rope_lst:
  if rope * idx > total:
    total = rope * idx
  idx += 1


print(total)