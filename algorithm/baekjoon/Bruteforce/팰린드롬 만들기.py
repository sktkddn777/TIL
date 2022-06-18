S = input()

for i in range(len(S)):
  tmp = S + S[:i][::-1]
  if tmp == tmp[::-1]:
    break

print(len(tmp))