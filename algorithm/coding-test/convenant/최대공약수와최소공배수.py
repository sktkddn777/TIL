def GCD(n1, n2):
    num = min(n1, n2)
    while (num > 0):
        if n1 % num == 0 and n2 % num == 0:
            return num
        num -= 1

    return -1

def LCM(n1, n2):
    x1, x2 = n1, n2
    while x1 != x2:
        if x1 > x2:
            x2 += n2
        else:
            x1 += n1

    return x1
 
n1, n2 = map(int, input().split())
print(GCD(n1, n2))
print(LCM(n1, n2))