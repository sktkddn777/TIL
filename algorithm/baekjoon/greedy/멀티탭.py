import sys
input = sys.stdin.readline

N, K = map(int, input().split())

appliances = list(map(int, input().split()))
appliance_dic = {}

for a in appliances[::-1]:
    appliance_dic[a] = appliance_dic.get(a, 0) + 1

plug = []
total = 0
for i, a in enumerate(appliances):
    if len(plug) < N:
        if a not in plug:
            plug.append(a)
        appliance_dic[a] -= 1

    else:
        if a not in plug:
            for x in plug:
                if appliance_dic[x] == 0:
                    plug.remove(x)
                    break

            if len(plug) == N:
                temp = []
                for x in appliances[i+1:]:
                    if x in plug and x not in temp:
                        temp.append(x)
                    if len(temp) == N:
                        plug.remove(temp[-1])
                        break

            plug.append(a)
            appliance_dic[a] -= 1
            total += 1
        else:
            appliance_dic[a] -= 1

print(total)
