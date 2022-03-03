n = int(input())
tile = [0] * 1001

tile[1], tile[2] = 1, 2

for i in range(3, 1001):
  tile[i] = (tile[i-1] + tile[i-2]) % 10007

print(tile[n])