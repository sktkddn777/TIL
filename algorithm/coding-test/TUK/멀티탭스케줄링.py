from collections import deque

N, K = map(int, input().split())
lst = list(map(int, input().split()))

appliance_dic = {}
for idx, app in enumerate(lst):
    if app in appliance_dic:
        appliance_dic[app].append(idx)
    else:
        appliance_dic[app] = deque([idx])
    
multitab = []

def checkRemove():
    remove_lst = []

    for t in multitab:
        if len(appliance_dic[t]) == 0:
            return t
        remove_lst.append((appliance_dic[t][0], t))
    return max(remove_lst)[1]

res = 0 
for x in lst:
    if x not in multitab:
        if len(multitab) < N:
            multitab.append(x)
            
        else:
            multitab.remove(checkRemove())
            multitab.append(x)
            res += 1

    appliance_dic[x].popleft()

print(res)

'''
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
'''