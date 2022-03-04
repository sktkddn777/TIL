N = int(input())

arr = [0] * (N + 1)
arr[1] = 0
x = 2

while x <= N:
  arr[x] = arr[x-1] + 1 
  if x % 3 == 0:
    arr[x] = arr[x//3] + 1 if arr[x//3] + 1 < arr[x] else arr[x]
  if x % 2 == 0:
    arr[x] = arr[x//2] + 1 if arr[x//2] + 1 < arr[x] else arr[x]
  x += 1
print(arr[-1])