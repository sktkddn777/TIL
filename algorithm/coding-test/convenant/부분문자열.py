S = list(input())
P = list(input())

def check():
    i = 0
    j = 0
    while i < len(S):
        if S[i] == P[j]:
            if len(S[i:]) < len(P):
                return 0
            res = 1
            for j in range(len(P)):
                if P[j] != S[i]:
                    res = 0
                    j = 0
                    i -= 1
                    break
                i += 1
                j += 1
            if res:
                return 1
        i += 1
    return 0

print(check())