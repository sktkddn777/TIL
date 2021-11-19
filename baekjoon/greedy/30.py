'''
검색했음
'''
'''
30으로 나누어 떨어지려면 각 자리수의 합이 3으로 나누어 떨어져야 한다는 
규칙을 알게되었다.
'''

N = list(input())
N = sorted(N, reverse=True)
res = ''.join(N)
N = [int(x) for x in N]

if sum(N) % 3 == 0 and N[-1] == 0:
  print(res)
else:
  print('-1')

