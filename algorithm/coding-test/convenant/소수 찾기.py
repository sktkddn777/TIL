prime_num = [True] * 1001
prime_num[0], prime_num[1] = False, False
for i in range(2, 33):
    j = 2
    while i * j <= 1000:
        prime_num[i * j] = False
        j += 1


N = int(input())
lst = map(int, input().split())

res = 0
for x in lst:
    if prime_num[x]:
        res += 1
print(res)