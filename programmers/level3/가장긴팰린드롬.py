def isPalindrome(x):
  if x == x[::-1]:
    return True


def solution(s):
  N = len(s)
  answer = 0
  for i in range(N):
    for j in range(i+1, N+1):
      if isPalindrome(s[i:j]):
        if answer < len(s[i:j]):
          answer = len(s[i:j])
  return answer

print(solution("abacde"))