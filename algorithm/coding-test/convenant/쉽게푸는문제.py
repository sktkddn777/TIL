lst = [0]
length = 1

while length <= 1000:
    lst += ([length] * length)
    length += 1

a, b = map(int, input().split())
print(sum(lst[a:b+1]))
