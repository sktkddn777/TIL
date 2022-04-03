'''
2022 kakao blind recruitment
programmers coding test practice
'''

def solution(id_list, report, k):
    answer = {k: 0 for k in id_list}
    report_dict = {k: [] for k in id_list}

    for r in report:
        x, y = r.split()
        if x not in report_dict[y]:
            report_dict[y].append(x)

    black_lst = []
    for x in report_dict:
        if len(report_dict[x]) >= k:
            black_lst.append(x)
    
    for black in black_lst:
        for x in report_dict[black]:
            answer[x] += 1
    
    return list(answer.values())

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))