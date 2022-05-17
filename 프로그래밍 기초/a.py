def solution(id_list, report, k):
    id_list_c = [0] * len(id_list)
    result = [0] * len(id_list)

    report_c = set(report)
    report_cc = list(report_c)

    for i in range(len(report_cc)):
        a = report_cc[i].split(' ')
        id_list_c[id_list.index(a[-1])] += 1

    for i in range(len(report_c)):
        a = report_cc[i].split(' ')
        if id_list_c[id_list.index(a[-1])] >= k:
            x = id_list.index(a[0])
            result[x] += 1













    # for i in range(len(report)):
    #     if report[i] not in report_c:
    #         report_c.append(report[i])



    # for i in range(len(report_c)):
    #     (a,b,c) = report_c[i].partition(' ')
    #     id_list_c[id_list.index(c)] += 1
    # #
    # for j in range(len(report_c)):
    #     (a, s, b) = report_c[j].partition(' ')
    #     if id_list_c[id_list.index(b)] >= k:
    #         x = id_list.index(a)
    #         result[x] += 1

    return result
# solution(['muzi', 'frodo', 'apeach', 'neo', 'con', 'ryan'],["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],2)
print(solution(['muzi', 'frodo', 'apeach', 'neo', 'con', 'ryan'],["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],2))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))