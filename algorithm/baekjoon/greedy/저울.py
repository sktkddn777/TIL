'''
수를 정렬하고 그에 따른 규칙을 찾아내야 한다.
이부분을 못찾아서 검색을 했다. 그 부분만 도움을 받고 나머지 고려사항은
혼자 했다.
'''
N = int(input())

num_lst = list(map(int, input().split()))
num_lst.sort()

res = 0

if num_lst[0] == 2:
  res = 1
else:
  for i in range(len(num_lst)):
    sum_num = sum(num_lst[:i])
    if sum_num + 1 < num_lst[i]:
      res = sum_num + 1
      break

if res == 0:
  res = sum(num_lst) + 1

print(res)