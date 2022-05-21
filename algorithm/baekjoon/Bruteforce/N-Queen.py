import sys
input = sys.stdin.readline

n = int(input())

ans = 0
row = [0] * n

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            row[x] = i
            flg = 1
            for j in range(x):
                if row[x] == row[j] or abs(row[x] - row[j]) == abs(x - j):
                    flg = 0
            
            if flg:    
                n_queens(x+1)

n_queens(0)
print(ans)