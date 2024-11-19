def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    # 동일한 유저에 대한 신고 1회로 처리
    report = set(report)
    
    # 신고당한 사람별 신고자 리스트
    reported = {}
    for i in report:
        a, r = i.split()
        if r not in reported:
            reported[r] = []
        reported[r].append(a)
    
    # k 이상일 경우 신고자들에게 메일 전송
    for r, a in reported.items():
        if len(a) >= k:
            for j in a:
                answer[id_list.index(j)] += 1
        
    return answer