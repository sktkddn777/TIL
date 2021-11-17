A, B = input().split()

res = 1
while int(B) > int(A):
  if B[-1] == '1':
    B = B[:-1]
  
  else:
    if int(B[-1]) % 2 != 0:
      break 
    
    B = str(int(B)//2)
  res += 1

if B == A:
  print(res)
else:
  print('-1')