def change_rev_mod3(n):
    res = ''
    while n > 0:
        n, mod = divmod(n, 3)
        res += str(mod)
    return res
        

def solution(n):
    str = change_rev_mod3(n)
    return  int(str, 3)

print(solution(45))