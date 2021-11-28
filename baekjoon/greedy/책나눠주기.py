import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())

  student = []
  book = [x for x in range(1, N+1)]
  for _ in range(M):
    student.append(list(map(int, input().split())))
  
  student.sort(key=lambda x:(x[1],x[0]))
  total = 0
  for x in student:
    for i in range(x[0], x[1]+1):
      if i in book:
        book.remove(i)
        total += 1
        break
  print(total)