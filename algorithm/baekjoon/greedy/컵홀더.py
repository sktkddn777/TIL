N = int(input())
seat = input()

holder = 1
s = 0
while s < len(seat):
  if seat[s] == 'S':
    s += 1
  else:
    s += 2
  holder += 1

if holder > len(seat):
  print(len(seat))
else:
  print(holder)
