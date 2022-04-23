N, K = map(int, input().split())
elec_lst = list(map(int, input().split()))
plug = []
res = 0

for i in range(K):
    if len(plug) < N and elec_lst[i] not in plug:
       plug.append(elec_lst[i])
    else:
        if elec_lst[i] not in plug:
            tmp_lst = [0] * N
            tmp = 1
            for j in range(i+1, K):
                if elec_lst[j] in plug:
                    idx = plug.index(elec_lst[j])
                    if tmp_lst[idx] == 0:
                        tmp_lst[idx] = tmp
                        tmp += 1
            if 0 in tmp_lst:
                plug[tmp_lst.index(0)] = elec_lst[i]
            else:
                plug[tmp_lst.index(max(tmp_lst))] = elec_lst[i]
            res += 1            

print(res)