'''
코딩 테스트 연습 2021 Dev-Matching 웹 백엔드 개발자
'''
def check_rank(x):
  if x < 2:
    return (6)
  else:
    return (7-x)
    

def solution(lottos, win_nums):
  ans = []
  dangchum = 0

  for lotto in lottos:
    if lotto in win_nums:
      dangchum += 1
  ans.append(check_rank(dangchum + lottos.count(0)))
  ans.append(check_rank(dangchum))

  return ans

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))