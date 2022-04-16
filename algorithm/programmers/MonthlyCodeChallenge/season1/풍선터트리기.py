def solution(a):
    min_idx = a.index(min(a))
    
    lst_left = a[:min_idx]
    lst_right = a[min_idx+1:]

    l_min = 1000000000
    r_min = 1000000000
    res = 0
    for x in lst_left:
        if x < l_min:
            l_min = x
            res += 1
    
    for x in lst_right[::-1]:
        if x < r_min:
            r_min = x
            res += 1
    
    return res + 1

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])