'''
코딩 테스트 연습 2021 Dev-Matching 웹 백엔드 개발자
'''

def rotate(arr, query):
  x, y = query[0], query[1]
  num = arr[x][y]
  first_num = arr[x][y]

  while x < query[2]:
    arr[x][y] = arr[x+1][y]
    if num > arr[x][y]:
      num = arr[x][y]
    x+=1
  while y < query[3]:
    arr[x][y] = arr[x][y+1]
    if num > arr[x][y]:
      num = arr[x][y]
    y+=1
  while x > query[0]:
    arr[x][y] = arr[x-1][y]
    if num > arr[x][y]:
      num = arr[x][y]
    x-=1

  while y > query[1]:
    arr[x][y] = arr[x][y-1]
    if num > arr[x][y]:
      num = arr[x][y]
    y-=1
  arr[x][y+1] = first_num
  return num

def solution(rows, columns, queries):
  arr = [[0] * columns for _ in range(rows)]
  for i in range(rows):
    for j in range(columns):
      arr[i][j] = (i * columns) + j + 1
  
  ans = []
  for query in queries:
    query = [x-1 for x in query]
    ans.append(rotate(arr, query))
  return ans

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))