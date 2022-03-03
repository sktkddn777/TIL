A = input()
word = input()

N = len(word)
start = 0
end = N
res = 0

while end <= len(A):
  if A[start:end] == word:
    res += 1
    start = end
    end = start + N
  else:
    start += 1
    end += 1
    
print(res)