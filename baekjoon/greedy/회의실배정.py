N = int(input())

meeting_room = []
total = 0

for _ in range(N):
  meeting_room.append(list(map(int, input().split())))

meeting_room = sorted(meeting_room, key=lambda x:(x[1],x[0]))

end = 0
for room in meeting_room:
  if room[0] >= end:
    end = room[1]
    total += 1

print(total)