lst = []
num = 0
for _ in range(10):
    p_out, p_in = map(int, input().split())
    num = num + p_in - p_out
    lst.append(num)
print(max(lst))