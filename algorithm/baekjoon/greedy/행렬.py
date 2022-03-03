'''
그냥 하나씩 비교해보면서 바꾸면 된다.
그리디 알고리즘에 대해 잘 생각해보자.
'''

def change(lst, X, Y):
  for i in range(X, X+3):
    for j in range(Y, Y+3):
      lst[i][j] = str(abs(int(lst[i][j])-1))

  return lst
N, M = map(int, input().split())

original = []
new_matrix = []
for i in range(2):
  for _ in range(N):
    original.append(list(input())) if i == 1 else new_matrix.append(list(input()))
res = 0

if N >= 3 or M >= 3:
  for x in range(N-2):
    for y in range(M-2):
      if original[x][y] != new_matrix[x][y]:
        original = change(original, x, y)
        res += 1
      if original == new_matrix:
        break
    if original == new_matrix:
      break


if original != new_matrix:
  print('-1')
else:
  print(res)