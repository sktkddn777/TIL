def make_bin(n):
    res = ''
    while n > 0:
        res += str(n%2)
        n //= 2
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    bin_rev = make_bin(N)
    for i in range(len(bin_rev)):
        if bin_rev[i] == '1':
            print(i, end=' ')
    print()
    