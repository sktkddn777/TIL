N = int(input())
lst = sorted(list(map(int, input().split())))

start , end = 0, N-1
min_h_dif, min_b_dif = abs(lst[start+1] - lst[start]), abs(lst[end] - lst[end-1])

while True:
    h_diff, b_diff = abs(lst[start+1] - lst[start]), abs(lst[end] - lst[end-1])

    if start + 2 != end - 1:
        if h_diff > b_diff:
            start += 1
            min_h_dif = min(min_h_dif, abs(lst[start] - lst[start+1]))
        else:
            end -= 1
            min_b_dif = min(min_b_dif, abs(lst[end] - lst[end-1]))
    else:
        break

print(min_h_dif - min_b_dif)



