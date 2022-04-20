lst = [1] * 10001
lst[0], lst[1] = 0, 0

for i in range(2, 101):
    j = 2
    while i * j <= 10000:
        lst[i*j] = 0
        j += 1

prime_lst = []
M = int(input())
N = int(input())
for i in range(len(lst[M:N+1])):
    if lst[M + i] == 1:
        prime_lst.append(M + i)

if len(prime_lst) == 0:
    print(-1)
else:
    print(sum(prime_lst))
    print(min(prime_lst))