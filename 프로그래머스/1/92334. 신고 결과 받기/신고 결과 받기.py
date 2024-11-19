def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}
    
    # 신고당한 사람 카운트 
    for r in set(report):
        reports[r.split()[1]] += 1
    
    # k 이상일 경우 신고자들 카운트
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
        
    return answer