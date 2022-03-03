
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B = sorted(B)
A = sorted(A, reverse=True)

total = 0
for i in range(len(A)):
  total += (A[i] * B[i])

print(total)
